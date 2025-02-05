import logging
from collections import OrderedDict
from django.test import TestCase
from apps.sistec.choices import InstituicaoChoices
from apps.sistec.domain.api_client import CicloMatriculaAPI
from apps.sistec.viewsets import CicloMatriculaSerializer

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class CicloMatriculaAPITest(TestCase):
    """
    Test case for the CicloMatriculaAPI.
    """

    @classmethod
    def setUpTestData(cls):
        cls.expected_responses = {
            "CAMPUS_ARACAJU": [
                OrderedDict([
                    ("pagina_atual", 1),
                    ("total_paginas", 3),
                    ("total_registros", 42),
                    ("ciclos", [
                        OrderedDict([
                            ("curso",
                             "ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - EDUCAÇÃO PRESENCIAL - AGO. 2023 / JAN. 2026"),
                            ("codigo", 3033988),
                            ("nome", "ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - EDUCAÇÃO PRESENCIAL"),
                            ("periodo", "21/08/2023 a 09/01/2026 em 2000 horas"),
                            ("status", "ATIVO"),
                            ("tipo_curso", "TECNOLOGIA")
                        ])
                    ])
                ])
            ],
            "CAMPUS_ESTANCIA": [
                OrderedDict([
                    ("pagina_atual", 1),
                    ("total_paginas", 1),
                    ("total_registros", 9),
                    ("ciclos", [
                        OrderedDict([
                            ("curso",
                             "TÉCNICO EM ELETROTÉCNICA - EDUCAÇÃO PRESENCIAL - SUBSEQUENTE - AGO. 2023 / JUL. 2025"),
                            ("codigo", 3031491),
                            ("nome", "TÉCNICO EM ELETROTÉCNICA - EDUCAÇÃO PRESENCIAL"),
                            ("periodo", "21/08/2023 a 20/07/2025 em 1200 horas"),
                            ("status", "ATIVO"),
                            ("tipo_curso", "TÉCNICO")
                        ])
                    ])
                ])
            ],
            "CAMPUS_ITABAIANA": [
                OrderedDict([
                    ("pagina_atual", 1),
                    ("total_paginas", 1),
                    ("total_registros", 7),
                    ("ciclos", [
                        OrderedDict([
                            ("curso",
                             "CURSO TÉCNICO DE NÍVEL MÉDIO EM AGRONEGÓCIO - EDUCAÇÃO PRESENCIAL - SUBSEQUENTE - AGO. 2023 / AGO. 2025"),
                            ("codigo", 3037360),
                            ("nome", "CURSO TÉCNICO DE NÍVEL MÉDIO EM AGRONEGÓCIO - EDUCAÇÃO PRESENCIAL"),
                            ("periodo", "21/08/2023 a 21/08/2025 em 1200 horas"),
                            ("status", "ATIVO"),
                            ("tipo_curso", "TÉCNICO")
                        ])
                    ])
                ])
            ],
            "CAMPUS_LAGARTO": [
                OrderedDict([
                    ("pagina_atual", 1),
                    ("total_paginas", 1),
                    ("total_registros", 16),
                    ("ciclos", [
                        OrderedDict([
                            ("curso",
                             "FÍSICA - EDUCAÇÃO PRESENCIAL - AGO. 2023 / JUN. 2027"),
                            ("codigo", 3031536),
                            ("nome", "FÍSICA - EDUCAÇÃO PRESENCIAL"),
                            ("periodo", "21/08/2023 a 30/06/2027 em 3275 horas"),
                            ("status", "ATIVO"),
                            ("tipo_curso", "LICENCIATURA")
                        ])
                    ])
                ])
            ],
            "CAMPUS_NOSSA_SENHORA_GLORIA": [
                OrderedDict([
                    ("pagina_atual", 1),
                    ("total_paginas", 1),
                    ("total_registros", 3),
                    ("ciclos", [
                        OrderedDict([
                            ("curso", "LATICÍNIOS - EDUCAÇÃO PRESENCIAL - MAR. 2023 / MAR. 2026"),
                            ("codigo", 2972213),
                            ("nome", "LATICÍNIOS - EDUCAÇÃO PRESENCIAL"),
                            ("periodo", "13/03/2023 a 13/03/2026 em 2640 horas"),
                            ("status", "ATIVO"),
                            ("tipo_curso", "TECNOLOGIA")
                        ])
                    ])
                ])
            ],
            "CAMPUS_SAO_CRISTOVAO": [
                OrderedDict([
                    ("pagina_atual", 1),
                    ("total_paginas", 1),
                    ("total_registros", 15),
                    ("ciclos", [
                        OrderedDict([
                            ("curso",
                             "TÉCNICO EM AGROINDÚSTRIA - EDUCAÇÃO PRESENCIAL - SUBSEQUENTE - AGO. 2023 / FEV. 2025"),
                            ("codigo", 3031556),
                            ("nome", "TÉCNICO EM AGROINDÚSTRIA - EDUCAÇÃO PRESENCIAL"),
                            ("periodo", "21/08/2023 a 21/02/2025 em 1216 horas"),
                            ("status", "ATIVO"),
                            ("tipo_curso", "TÉCNICO")
                        ])
                    ])
                ])
            ],
            "CAMPUS_NOSSA_SENHORA_SOCORRO": [
                OrderedDict([
                    ("pagina_atual", 1),
                    ("total_paginas", 1),
                    ("total_registros", 6),
                    ("ciclos", [
                        OrderedDict([
                            ("curso",
                             "TÉCNICO EM MANUTENÇÃO E SUPORTE EM INFORMÁTICA - EDUCAÇÃO PRESENCIAL - SUBSEQUENTE - AGO. 2023 / DEZ. 2024"),
                            ("codigo", 3031582),
                            ("nome", "TÉCNICO EM MANUTENÇÃO E SUPORTE EM INFORMÁTICA - EDUCAÇÃO PRESENCIAL"),
                            ("periodo", "21/08/2023 a 06/12/2024 em 1000 horas"),
                            ("status", "ATIVO"),
                            ("tipo_curso", "TÉCNICO")
                        ])
                    ])
                ])
            ],
            "CAMPUS_POCO_REDONDO": [
                OrderedDict([
                    ("pagina_atual", 1),
                    ("total_paginas", 1),
                    ("total_registros", 1),
                    ("ciclos", [
                        OrderedDict([
                            ("curso",
                             "EDUCAÇÃO DE JOVENS E ADULTOS INTEGRADA À EDUC. PROF. TEC. EJA/EPT COM ÊNFASE NA EDUCAÇÃO DO CAMPO - EDUCAÇÃO PRESENCIAL - AGO. 2023 / ABR. 2024"),
                            ("codigo", 3028295),
                            ("nome", "EDUCAÇÃO DE JOVENS E ADULTOS INTEGRADA À EDUC. PROF. TEC.  EJA/EPT COM ÊNFASE NA EDUCAÇÃO DO CAMPO - EDUCAÇÃO PRESENCIAL"),
                            ("periodo", "04/08/2023 a 23/04/2024 em 160 horas"),
                            ("status", "CONCLUÍDO"),
                            ("tipo_curso", "FORMAÇÃO INICIAL")
                        ])
                    ])
                ])
            ],
            "CAMPUS_PROPRIA": [
                OrderedDict([
                    ("pagina_atual", 1),
                    ("total_paginas", 1),
                    ("total_registros", 3),
                    ("ciclos", [
                        OrderedDict([
                            ("curso",
                             "TÉCNICO EM MANUTENÇÃO E SUPORTE EM INFORMÁTICA - EDUCAÇÃO PRESENCIAL - SUBSEQUENTE - AGO. 2023 / JAN. 2025"),
                            ("codigo", 3028292),
                            ("nome",
                             "TÉCNICO EM MANUTENÇÃO E SUPORTE EM INFORMÁTICA - EDUCAÇÃO PRESENCIAL"),
                            ("periodo", "21/08/2023 a 21/01/2025 em 1000 horas"),
                            ("status", "ATIVO"),
                            ("tipo_curso", "TÉCNICO")
                        ])
                    ])
                ])
            ],
            "CAMPUS_TOBIAS_BARRETO": [
                OrderedDict([
                    ("pagina_atual", 1),
                    ("total_paginas", 1),
                    ("total_registros", 4),
                    ("ciclos", [
                        OrderedDict([
                            ("curso",
                             "TÉCNICO EM COMÉRCIO - EDUCAÇÃO PRESENCIAL - SUBSEQUENTE - MAR. 2023 / JUL. 2024"),
                            ("codigo", 2969861),
                            ("nome",
                             "TÉCNICO EM COMÉRCIO - EDUCAÇÃO PRESENCIAL"),
                            ("periodo", "13/03/2023 a 26/07/2024 em 871 horas"),
                            ("status", "ATIVO"),
                            ("tipo_curso", "TÉCNICO")
                        ])
                    ])
                ])
            ],
        }

    def test_list(self):
        logger.info("Iniciando o teste da listagem de ciclos de matrícula")
        for instituicao in list(InstituicaoChoices)[1:]:
            logger.debug(f"Testando a instituição: {instituicao.label}")
            self.api = CicloMatriculaAPI(instituicao.value)

            # Chamando a API real
            result = self.api.list(2023, [])
            logger.debug(f"Resultado da API para {instituicao.label}: {result}")

            assert result[0].get("ciclos")[0] == self.expected_responses[instituicao.name][0].get("ciclos")[0]
            logger.info(f"Teste para {instituicao.label} concluído com sucesso")

        logger.info("Todos os testes de listagem de ciclos de matrícula foram concluídos")

if __name__ == "__main__":
    TestCase.main()