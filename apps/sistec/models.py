from django.db import models

from apps.sigaa.models.comum import SigCampus
from apps.sigaa.models.public import SigCurso


class Instituicao(models.Model):
    codigo = models.CharField("Código", max_length=10, unique=True)
    sig_unidade = models.ForeignKey(SigCampus, models.DO_NOTHING)

    class Meta:
        abstract = True


class Curso(models.Model):
    id_sistec = models.PositiveIntegerField("ID SISTEC", unique=True)
    sig_curso = models.ForeignKey(SigCurso, models.DO_NOTHING)

    class Meta:
        abstract = True


class CicloMatricula(models.Model):
    instituicao = models.ForeignKey('Instituicao', models.DO_NOTHING)

    class Meta:
        abstract = True
