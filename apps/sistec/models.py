from django.db import models

from apps.sigaa.models.comum import SigCampus
from apps.sigaa.models.public import SigCurso


class Instituicao(models.Model):
    codigo = models.CharField("Código", max_length=10, unique=True)
    descricao = models.CharField("Descrição", max_length=255)
    # sig_unidade = models.ForeignKey(SigCampus, models.DO_NOTHING, null=True)

    class Meta:
        db_table = "sistec_instituicao"


class Curso(models.Model):
    id_sistec = models.PositiveIntegerField("ID SISTEC", unique=True)
    descricao = models.CharField("Descrição", max_length=255)
    instituicao = models.ForeignKey(Instituicao, models.DO_NOTHING)
    # sig_curso = models.ForeignKey(SigCurso, models.DO_NOTHING, null=True)

    class Meta:
        db_table = "sistec_curso"


class CicloMatricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, models.DO_NOTHING)

    class Meta:
        db_table = "sistec_ciclo_matricula"
