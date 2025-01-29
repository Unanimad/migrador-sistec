from datetime import timedelta
from typing import List

from django.utils import timezone

from django.db import models
from django.db.models import Q, Max, CharField
from django.db.models.functions import Concat


class SigDiscenteManager(models.Manager):
    def sem_vinculos(self, ids: List[int]) -> models.QuerySet:
        to_ = timezone.now().today()
        to_ -= timedelta(days=30)

        qs = ~Q(status_discente__id_status__in=[1, 14, 8, 9, 2, 11, 5, -1]) & \
             Q(sigmovimentacaoaluno__sigestornomovimentacaoaluno__isnull=True) & \
             Q(sigmovimentacaoaluno__data_ocorrencia__lte=to_) & \
             Q(id_discente__in=ids)

        return self.filter(qs)

    def ativos(self) -> models.QuerySet:
        qs = Q(sigdiscenteturma__situacao_matricula_id=2)
        qs &= Q(status_discente_id__in=[1, 9, 8])
        return self.filter(qs).distinct()