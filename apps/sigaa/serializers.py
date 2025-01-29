from rest_framework import serializers

from .models import SigDiscente


class DiscenteSerializer(serializers.Serializer):
    id_turma = serializers.IntegerField()
    id_pessoa = serializers.IntegerField()
    cpf = serializers.IntegerField()
    nome = serializers.CharField()
    matricula = serializers.IntegerField()
    id_discente = serializers.IntegerField()
    id_situacao_matricula = serializers.IntegerField()
    situacao = serializers.CharField()


class DocenteSerializer(serializers.Serializer):
    id_turma = serializers.IntegerField()
    id_docente = serializers.IntegerField()
    id_pessoa = serializers.IntegerField()
    nome = serializers.CharField()
    cpf = serializers.CharField()


class TurmaSerializer(serializers.Serializer):
    id_turma = serializers.IntegerField()
    ano = serializers.IntegerField()
    periodo = serializers.IntegerField()
    nivel_ensino = serializers.CharField()
    sala = serializers.CharField()
    campus = serializers.CharField()
    data_inicio = serializers.DateField()
    data_fim = serializers.DateField()
    descricao_horario = serializers.CharField()
    codigo_disciplina = serializers.CharField()
    nome_disciplina = serializers.CharField()
    ementa = serializers.CharField()
    ch_disciplina = serializers.CharField()
    codigo_curso = serializers.CharField()
    nome_curso = serializers.CharField()
    alunos_matriculados = serializers.IntegerField()

    docentes = DocenteSerializer(required=False, many=True)
    discentes = DiscenteSerializer(required=False, many=True)
