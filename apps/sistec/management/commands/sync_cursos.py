from django.core.management import BaseCommand

from apps.sistec.domain import CursosAPI
from apps.sistec.models import Instituicao, Curso


class Command(BaseCommand):
    def handle(self, *args, **options):
        bulk_create = []
        for instituicao in Instituicao.objects.all():
            api = CursosAPI(instituicao.codigo)

            bulk_create.extend(Curso(id_sistec=int(curso['id']), descricao=curso['name'], instituicao=instituicao)
                               for curso in api.list())

        Curso.objects.bulk_create(bulk_create, ignore_conflicts=True)
