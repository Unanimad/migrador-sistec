from django.db import models

from apps.sigaa.models.ensino import SigDisciplina

class SigModalidade(models.Model):
    id_modalidade_curso_tecnico = models.IntegerField(primary_key=True, db_column='id_modalidade_curso_tecnico')
    descricao = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = u'"tecnico"\".\"modalidade_curso_tecnico"'
        default_permissions = ()


class SigEstruturaCurricular(models.Model):
    id_estrutura_curricular = models.IntegerField(primary_key=True, db_column='id_estrutura_curricular')
    modalidade = models.ForeignKey(SigModalidade, on_delete=models.PROTECT, db_column='id_modalidade_curso_tecnico')

    class Meta:
        managed = False
        db_table = u'"tecnico\".\"estrutura_curricular_tecnica"'
        default_permissions = ()


class SigModuloDisciplina(models.Model):
    id_modulo = models.IntegerField(primary_key=True, db_column='id_modulo')
    disciplina = models.ForeignKey(SigDisciplina, on_delete=models.RESTRICT, db_column='id_disciplina')

    class Meta:
        managed = False
        db_table = u'"tecnico\".\"modulo_disciplina'
        default_permissions = ()


class SigModuloCurricular(models.Model):
    id_modulo_curricular = models.IntegerField(primary_key=True, db_column='id_modulo_curricular')
    modulo_disciplina = models.ForeignKey(SigModuloDisciplina, on_delete=models.PROTECT, db_column='id_modulo')
    estrutura_curricular = models.ForeignKey(
        SigEstruturaCurricular, on_delete=models.PROTECT,
        db_column='id_estrutura_curricular'
    )

    class Meta:
        managed = False
        db_table = u'"tecnico"\".\"modulo_curricular"'
        default_permissions = ()