from collections import OrderedDict

from django.test import TestCase

from apps.sistec.choices import IntituicaoChoices
from apps.sistec.domain.api_client import CicloMatriculaAPI
from apps.sistec.viewsets import CicloMatriculaSerializer

# python manage.py test apps.sistec.tests.test_ciclo_matricula

class CicloMatriculaAPITest(TestCase):
    """
    Test case for the CicloMatriculaAPI.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up the test data.
        """
        cls.instituicao = IntituicaoChoices.CAMPUS_ARACAJU
        cls.api = CicloMatriculaAPI(cls.instituicao.value)

    def setUp(self):
        """
        Set up the test case.
        """
        pass

    def test_list_sao_cristovao(self):
        """
        Test the list method of CicloMatriculaAPI.
        This test verifies that the API returns the expected response.
        """
        expected_response = [
            OrderedDict([
                ('pagina_atual', 1),
                ('total_paginas', 1),
                ('total_registros', 15),
                ('ciclos', [
                    OrderedDict([
                        ('curso',
                         'TÉCNICO EM AGROINDÚSTRIA - EDUCAÇÃO PRESENCIAL - SUBSEQUENTE - AGO. 2023 / FEV. 2025'),
                        ('codigo', 3031556),
                        ('nome', 'TÉCNICO EM AGROINDÚSTRIA - EDUCAÇÃO PRESENCIAL'),
                        ('periodo', '21/08/2023 a 21/02/2025 em 1216 horas'),
                        ('status', 'ATIVO'),
                        ('tipo_curso', 'TÉCNICO')
                    ])
                ])
            ])
        ]

        # Chamando a API real
        result = self.api.list(2023, [])

        # Validando com o serializer real
        assert result[0].get("ciclos")[0] == expected_response[0].get("ciclos")[0]


if __name__ == '__main__':
    TestCase.main()
