from django.db import models

from apps.sigaa.models.public import SigCurso
from apps.sigaa.models.ensino import SigDisciplina

class SigGraduacaoCurriculo(models.Model):
    id_curriculo = models.IntegerField(primary_key=True, db_column="id_curriculo")
    curso = models.ForeignKey(SigCurso, on_delete=models.RESTRICT, db_column="id_curso")

    class Meta:
        managed = False
        db_table = u'"graduacao\".\"curriculo"'
        default_permissions = ()


class SigGraduacaoCurriculoComponente(models.Model):
    id_curriculo_componente = models.IntegerField(primary_key=True, db_column="id_curriculo_componente")
    disciplina = models.ForeignKey(SigDisciplina, on_delete=models.RESTRICT, db_column="id_disciplina")
    curriculo = models.ForeignKey(SigGraduacaoCurriculo, on_delete=models.RESTRICT, db_column="id_curriculo")

    class Meta:
        managed = False
        db_table = u'"graduacao\".\"curriculo_componente"'
        default_permissions = ()