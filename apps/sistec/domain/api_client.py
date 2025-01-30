import requests

from typing import List

from django.conf import settings

from apps.sistec.domain import SISTEC
from apps.sistec.viewsets import CicloMatriculaSerializer


class SisTecAPI:
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
        "connection": "keep-alive",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": settings.COOKIE_SISTEC,
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


class CicloMatriculaAPI(SisTecAPI):
    url = SISTEC.url_base + "/gridciclo/turmas/ano"

    def list(self, ano: int, data: List[dict], pagina: int = 1):
        response = requests.post(f"{self.url}/{ano}", headers=self.headers, data={"pagina": pagina})
        response_data = response.json()

        serializer = CicloMatriculaSerializer(data=response_data)
        breakpoint()
        if serializer.is_valid():
            data.append(serializer.data)
            breakpoint()
            if serializer.data["pagina_atual"] != serializer.data["total_paginas"]:
                pagina += 1
                self.list(ano, data, pagina)
        else:
            data.append(serializer.errors)
        return data
