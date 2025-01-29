from django.db import models

from apps.sigaa.models.public import SigStatusDiscente, SigDiscente, SigCurso
from apps.sigaa.models.rh import SigServidor


class SigTipoMovimentacaoAluno(models.Model):
    id_tipo_movimentacao_aluno = models.IntegerField(primary_key=True)
    descricao = models.TextField()
    grupo = models.CharField(max_length=2, null=True)
    ativo = models.BooleanField()
    status_discente = models.ForeignKey(SigStatusDiscente, on_delete=models.RESTRICT, db_column="statusdiscente")
    graduacao = models.BooleanField()
    stricto = models.BooleanField()
    todos = models.BooleanField()
    perda = models.BooleanField()
    medio = models.BooleanField()

    class Meta:
        managed = False
        db_table = u'"ensino\".\"tipo_movimentacao_aluno"'
        default_permissions = ()


class SigMovimentacaoAluno(models.Model):
    id_movimentacao_aluno = models.IntegerField(primary_key=True)
    discente = models.ForeignKey(SigDiscente, on_delete=models.RESTRICT, db_column="id_discente")
    tipo_movimentacao = models.ForeignKey(SigTipoMovimentacaoAluno, on_delete=models.RESTRICT,
                                          db_column="id_tipo_movimentacao_aluno")
    data_ocorrencia = models.DateTimeField()
    ativo = models.BooleanField()
    ano_referencia = models.PositiveSmallIntegerField()
    periodo_referencia = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = u'"ensino\".\"movimentacao_aluno"'
        default_permissions = ()


class SigEstornoMovimentacaoAluno(models.Model):
    id_estorno_movimentacao_aluno = models.IntegerField(primary_key=True)
    data_estorno = models.DateTimeField()
    movimentacao = models.ForeignKey(SigMovimentacaoAluno, on_delete=models.RESTRICT, db_column="id_movimentacao_aluno")

    class Meta:
        managed = False
        db_table = u'"ensino\".\"estorno_movimentacao_aluno"'
        default_permissions = ()


class SigDisciplinaDetalhes(models.Model):
    id_disciplina_detalhes = models.IntegerField(primary_key=True, db_column="id_componente_detalhes")
    nome = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = u'"ensino\".\"componente_curricular_detalhes"'
        default_permissions = ()


class SigDisciplina(models.Model):
    id_disciplina = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=20)
    detalhe = models.ForeignKey(SigDisciplinaDetalhes, on_delete=models.RESTRICT, db_column="id_detalhe")
    curso = models.ForeignKey(SigCurso, on_delete=models.RESTRICT, db_column="id_curso", null=True)

    class Meta:
        managed = False
        db_table = u'"ensino\".\"componente_curricular"'
        default_permissions = ()


class SigSituacaoTurma(models.Model):
    id_situacao = models.IntegerField(primary_key=True, db_column="id_situacao_turma")
    descricao = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = u'"ensino\".\"situacao_turma"'
        default_permissions = ()


class SigTurma(models.Model):
    id_turma = models.IntegerField(primary_key=True)
    ano = models.IntegerField()
    periodo = models.IntegerField()
    codigo = models.CharField(max_length=30)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    curso = models.ForeignKey(SigCurso, on_delete=models.RESTRICT, db_column="id_curso", null=True)
    disciplina = models.ForeignKey(SigDisciplina, on_delete=models.RESTRICT, db_column="id_disciplina")
    situacao = models.ForeignKey(SigSituacaoTurma, on_delete=models.RESTRICT, db_column="id_situacao_turma")

    class Meta:
        managed = False
        db_table = u'"ensino\".\"turma"'
        default_permissions = ()


class SigDocenteTurma(models.Model):
    id_docente_turma = models.IntegerField(primary_key=True, db_column="id_docente_turma")
    turma = models.ForeignKey(SigTurma, on_delete=models.RESTRICT, db_column="id_turma")
    docente = models.ForeignKey(SigServidor, on_delete=models.RESTRICT, db_column="id_docente",
                                related_name="docente_turma")
    ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = u'"ensino\".\"docente_turma"'
        default_permissions = ()


class SigSituacaoMatricula(models.Model):
    id_situacao_matricula = models.IntegerField(primary_key=True, db_column="id_situacao_matricula")
    descricao = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = u'"ensino\".\"situacao_matricula"'
        default_permissions = ()


class SigDiscenteTurma(models.Model):
    id_discente_turma = models.IntegerField(primary_key=True, db_column="id_matricula_componente")
    turma = models.ForeignKey(SigTurma, on_delete=models.RESTRICT, db_column="id_turma")
    discente = models.ForeignKey(SigDiscente, on_delete=models.RESTRICT, db_column="id_discente")
    situacao_matricula = models.ForeignKey(SigSituacaoMatricula, on_delete=models.RESTRICT,
                                           db_column="id_situacao_matricula")

    class Meta:
        managed = False
        db_table = u'"ensino\".\"matricula_componente"'
        default_permissions = ()