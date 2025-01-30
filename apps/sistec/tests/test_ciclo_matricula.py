from django.test import TestCase
from unittest.mock import patch, Mock
from apps.sistec.domain.api_client import CicloMatriculaAPI
from apps.sistec.viewsets import CicloMatriculaSerializer


class CicloMatriculaAPITest(TestCase):
    def test_list(self):
        # Instância da API real
        api = CicloMatriculaAPI()
        data = []

        # Chamando a API real
        result = api.list(2023, data)

        # Validando com o serializer real
        serializer = CicloMatriculaSerializer(data=result, many=True)
        self.assertTrue(serializer.is_valid())

        # Garantindo que o retorno é esperado
        self.assertIsInstance(serializer.data, list)
        self.assertGreater(len(serializer.data), 0)


if __name__ == '__main__':
    TestCase.main()
