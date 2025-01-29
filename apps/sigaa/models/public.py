from django.db import models

from apps.sigaa.models.comum import SigPessoa, SigCampus
from apps.sigaa.managers import SigDiscenteManager


class SigStatusDiscente(models.Model):
    id_status = models.IntegerField(primary_key=True, db_column="status")
    descricao = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = "status_discente"
        default_permissions = ()


class SigDiscente(models.Model):
    id_discente = models.IntegerField(primary_key=True)
    matricula = models.PositiveBigIntegerField()
    pessoa = models.ForeignKey(SigPessoa, on_delete=models.RESTRICT, db_column="id_pessoa")
    status_discente = models.ForeignKey(SigStatusDiscente, on_delete=models.RESTRICT, db_column="status")
    ano_ingresso = models.PositiveSmallIntegerField(db_column="ano_ingresso")
    periodo_ingresso = models.PositiveSmallIntegerField(db_column="periodo_ingresso")

    objects = SigDiscenteManager()

    class Meta:
        managed = False
        db_table = "discente"
        default_permissions = ()


class SigCurso(models.Model):
    id_curso = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    nivel = models.CharField(max_length=1)
    campus = models.ForeignKey(SigCampus, on_delete=models.RESTRICT, db_column="id_unidade")

    class Meta:
        managed = False
        db_table = "curso"
        default_permissions = ()

    def __str__(self):
        return self.nome