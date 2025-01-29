from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TurmaSerializer, DiscenteSerializer, DocenteSerializer


class TurmaViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TurmaSerializer

    def list(self, request):

        query = []
        if query:
            serializer = TurmaSerializer()
            return Response(serializer.data)
        else:
            return Response({})

    def retrieve(self, request, pk=None):

        instance = Turma(id_turma=pk).get()
        serializer = TurmaSerializer(instance)

        if request.GET.get('extended'):
            extended = self.__extended(pk)

            return Response({**serializer.data, **extended})

        return Response(serializer.data)

    @staticmethod
    def __extended(pk):
        discentes = SigDiscente().list(query=f'mc.id_turma = {pk}')
        discentes = DiscenteSerializer(discentes, many=True)

        docentes = Docente().list(query=f'et.id_turma = {pk}')
        docentes = DocenteSerializer(docentes, many=True)

        return {'discentes': discentes.data, 'docentes': docentes.data}


class DiscenteViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DiscenteSerializer

    def list(self, request):
        query = []

        if request.GET.get('id_pessoa', None):
            list_ = request.GET.getlist('id_pessoa')
            query.append(f"di.id_pessoa in ({','.join([pk for pk in list_])})")

        if request.GET.get('id_discente', None):
            list_ = request.GET.getlist('id_discente')
            query.append(f"di.id_discente in ({','.join([pk for pk in list_])})")

        if request.GET.get('id_turma', None):
            list_ = request.GET.getlist('id_turma')
            query.append(f"mc.id_turma in ({','.join([pk for pk in list_])})")

        if request.GET.get('id_situacao_matricula', None):
            list_ = request.GET.getlist('id_situacao_matricula')
            query.append(f"mc.id_situacao_matricula in ({','.join([pk for pk in list_])})")

        if request.GET.get('limit', None):
            query.append(f"limit {request.GET['limit']}")

        if query:
            query = ' and '.join(query)

            instances = SigDiscente().list(query=query)

            if len(instances) > 1:
                many = True
            elif len(instances) == 1:
                instances = instances[0]
                many = False
            else:
                pass

            serializer = DiscenteSerializer(instances, many=many)

            return Response(serializer.data)

        else:
            return Response({'err': 'Necessário informar uma query para consulta!'})


class DocenteViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DocenteSerializer

    def list(self, request):
        query = []

        if request.GET.get('id_pessoa', None):
            list_ = request.GET.getlist('id_pessoa')
            query.append(f"id_pessoa in ({','.join([pk for pk in list_])})")

        if request.GET.get('id_docente', None):
            list_ = request.GET.getlist('id_docente')
            query.append(f"id_docente in ({','.join([pk for pk in list_])})")

        if request.GET.get('id_turma', None):
            list_ = request.GET.getlist('id_turma')
            query.append(f"id_turma in ({','.join([pk for pk in list_])})")

        if request.GET.get('limit', None):
            query.append(f"limit {request.GET['limit']}")

        if query:
            query = ' and '.join(query)

            instances = Docente().list(query=query)

            if len(instances) > 1:
                many = True
            elif len(instances) == 1:
                instances = instances[0]
                many = False
            else:
                pass

            serializer = DocenteSerializer(instances, many=many)

            return Response(serializer.data)
        else:
            return Response({'err': 'Necessário informar uma query para consulta!'})

