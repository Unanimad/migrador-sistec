from rest_framework import serializers

from apps.sistec.models import CicloMatricula


class CicloSerializer(serializers.Serializer):
    curso = serializers.CharField()
    codigo_do_ciclo = serializers.IntegerField(source="codigo")
    nome_do_ciclo = serializers.CharField(source="nome")
    periodo_do_ciclo = serializers.CharField(source="periodo")
    status_do_ciclo = serializers.CharField(source="status")
    tipo_do_curso = serializers.CharField(source="tipo_curso")


class CicloMatriculaSerializer(serializers.Serializer):
    pagina_atual = serializers.IntegerField()
    total_paginas = serializers.IntegerField()
    total_registros = serializers.IntegerField()
    ciclos = CicloSerializer(many=True)


# class PostCicloMatriculaSerializer(serializers.ModelSerializer):
#     st_ciclo = serializers.IntegerField()
#     st_previsto = serializers.CharField(allow_blank=True, required=False)
#     st_dentro_periodo = serializers.CharField(allow_blank=True, required=False)
#     coInstituicao = serializers.CharField()
#     tipoCurso = serializers.IntegerField()
#     curso = serializers.IntegerField()
#     uab = serializers.CharField()
#     etec = serializers.CharField()
#     obrigatorioEtec = serializers.CharField()
#     modalidadeEnsino = serializers.IntegerField()
#     tipoOferta = serializers.IntegerField()
#     ppAssociado = serializers.CharField(allow_blank=True, required=False)
#     nivelOferta = serializers.CharField(allow_blank=True, required=False)
#     dtInicial = serializers.DateField()
#     dtFinal = serializers.DateField(allow_blank=True, required=False)
#     st_estagio = serializers.IntegerField()
#     cargaHorariaEstagio = serializers.CharField(allow_blank=True, required=False)
#     cargaHoraria = serializers.CharField(allow_blank=True, required=False)
#     nomeCiclo = serializers.CharField()
#     anexo = serializers.FileField()
#     idCiclo = serializers.CharField(allow_blank=True, required=False)
#     coCurso = serializers.IntegerField()
#     sistemaEnsino = serializers.IntegerField()
#     coPoloCicloMatricula = serializers.CharField(allow_blank=True, required=False)
#     coPortfolio = serializers.CharField(allow_blank=True, required=False)
#     coCicloMatricula = serializers.CharField(allow_blank=True, required=False)
#     projeto_pedagogico_removido = serializers.IntegerField()
#     institutoFederal = serializers.IntegerField()
#     isTermoAssinado = serializers.IntegerField()
#     justificativa_gestor_mec = serializers.CharField(allow_blank=True, required=False)
#     vagasPrevistas = serializers.CharField(allow_blank=True, required=False)
#     vagasOfertadas = serializers.CharField(allow_blank=True, required=False)
#     totalInscritos = serializers.CharField(allow_blank=True, required=False)
#     nuCargaHorariaMinima = serializers.IntegerField()
#
#     class Meta:
#         model = CicloMatricula
#         fields = '__all__'
