import requests

from typing import List
from urllib.parse import urlencode

from bs4 import BeautifulSoup

from django.conf import settings

from apps.sistec.domain import SISTEC
from apps.sistec.viewsets.ciclos_matricula import CicloMatriculaSerializer
from apps.sistec.viewsets.cursos import CursoSerializer


class SisTecAPI:
    url_base = SISTEC.url_base

    def __init__(self, instituicao_codigo):
        self.instituicao_codigo = instituicao_codigo

        self.cookies = {
            "PHPSESSID": "r4v4c7fhmk9l2mjbgcib15enf5",
            "BIGipServerPOOL_SISTEC": "3292561930.20480.0000",
            "perfil_cookie": "GESTOR+DA+UNIDADE+DE+ENSINO",
            "co_usuario": str(self.instituicao_codigo)
        }

        self.headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
            "connection": "keep-alive",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
            "x-kl-saas-ajax-request": "Ajax_Request",
            "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        }
        self.login()

    def login(self):
        url = f"{self.url_base}/index/index"
        dados = {"tipo": self.instituicao_codigo, "acao": "", "qtdPerfis": 11}
        dados = urlencode(dados)
        response = self.do_request(url, "POST", params=dados)
        response.raise_for_status()

    def __set_cookie(self, cookies=None):
        if not cookies:
            cookies = settings.COOKIE_SISTEC.format(instituicao_codigo=self.instituicao_codigo)
        self.headers["cookie"] = cookies

    def save_csv(self, url, *args, **kwargs):
        response = self.do_request(url, "POST", stream=True, *args, **kwargs)
        file_name = f"{self.__class__.__name__}_{self.instituicao_codigo}"
        for key, value in kwargs["data"].items():
            file_name += f"_{value}" if value else ""

        file_name = f"{file_name}.csv"
        with open(file_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)

        return file_name

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
            response = requests.request(method, url, headers=self.headers, cookies=self.cookies, *args, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            raise e


class CicloMatriculaAPI(SisTecAPI):

    def list(self, ano: int, data: List[dict], pagina: int = 1):
        url = self.url_base + "/gridciclo/turmas/ano"
        response = self.do_request(f"{url}/{ano}", "POST", data={"pagina": pagina})
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

    def download_csv(self, ano) -> str:
        url = self.url_base + "/gridciclo/exportar-ciclo-turmas/"
        data = {
            "Ano": ano,
            "coCiclo": None,
            "noInstituicao": None,
            "tipoCurso": None,
            "stCicloName": None,
            "acoes": None,
        }

        file_name = self.save_csv(url, data=data)
        return file_name


class CursosAPI(SisTecAPI):
    def list(self, tipo_curso: str = None):
        url = self.url_base + "/admciclomatricula/cursos"
        response = self.do_request(url, "POST", data={"tipoCurso": tipo_curso})
        response_data = self.convert_keys_to_snake_case(response.json())
        dados = response_data.pop("mensagem")

        soup = BeautifulSoup(dados, "html.parser")
        serializer = CursoSerializer(data=[
            {"id": option.get("value"), "name": option.text.strip().upper()} for option in soup.find_all("option")[1:]
            # ignore first blank option
        ], many=True)

        if serializer.is_valid():
            return serializer.validated_data

        return serializer.errors
