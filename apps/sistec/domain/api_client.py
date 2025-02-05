import requests

from typing import List

from django.conf import settings

from apps.sistec.domain import SISTEC
from apps.sistec.viewsets import CicloMatriculaSerializer


class SisTecAPI:
    def __init__(self, instituicao_codigo):

        self.instituicao_codigo = instituicao_codigo

        self.headers = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
            "connection": "keep-alive",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": settings.COOKIE_SISTEC.format(instituicao_codigo=self.instituicao_codigo),
            "origin": "https://sistec.mec.gov.br",
            "referer": "https://sistec.mec.gov.br/index/index",
            "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
            "x-kl-saas-ajax-request": "Ajax_Request",
            "x-request": "JSON",
            "x-requested-with": "XMLHttpRequest"
        }
        # response = self.login()
        # self.__set_cookie(cookies=response.headers["Set-Cookie"])

    def login(self):
        url = "https://sistec.mec.gov.br/index/index/"
        dados = {"tipo": self.instituicao_codigo}
        response = requests.post(url, headers=self.headers, data=dados)
        response.raise_for_status()
        return response

    def __set_cookie(self, cookies=None):
        if not cookies:
            cookies = settings.COOKIE_SISTEC.format(instituicao_codigo=self.instituicao_codigo)
        self.headers["cookie"] = cookies

    @staticmethod
    def convert_keys_to_snake_case(data: dict):
        import re
        import unicodedata
        def convert(item):
            if isinstance(item, dict):
                return {re.sub(r'(?<!^)(?=[A-Z])', '_',
                               unicodedata.normalize('NFKD', k).encode('ascii', 'ignore').decode(
                                   'ascii')).lower().replace(" ", "_").replace("__", "_"):
                            convert(v) for k, v in
                        item.items()}
            elif isinstance(item, list):
                return [convert(i) for i in item]
            else:
                return item

        return convert(data)

    def do_request(self, url, method, *args, **kwargs):
        try:
            response = requests.request(method, url, headers=self.headers, *args, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            raise e


class CicloMatriculaAPI(SisTecAPI):
    url = SISTEC.url_base + "gridciclo/turmas/ano"

    def list(self, ano: int, data: List[dict], pagina: int = 1):
        response = self.do_request(f"{self.url}/{ano}", "POST", data={"pagina": pagina})
        response_data = self.convert_keys_to_snake_case(response.json())

        dados = response_data
        dados["ciclos"] = dados.pop("dados")
        serializer = CicloMatriculaSerializer(data=response_data)
        if serializer.is_valid():
            data.append(serializer.validated_data)
            if serializer.data["pagina_atual"] != serializer.data["total_paginas"]:
                pagina += 1
                self.list(ano, data, pagina)
        else:
            data.append(serializer.errors)
        return data
