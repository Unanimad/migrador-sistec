from django.db.models.enums import TextChoices


class InstituicaoChoices(TextChoices):
    NAOINFORMADO = "", "Selecione..."
    CAMPUS_ARACAJU = "8474494", "GESTOR DA UNIDADE DE ENSINO - INSTITUTO FEDERAL DE SERGIPE - CAMPUS ARACAJU"
    CAMPUS_ESTANCIA = "8474496", "GESTOR DA UNIDADE DE ENSINO - INSTITUTO FEDERAL DE SERGIPE - CAMPUS ESTÂNCIA"
    CAMPUS_ITABAIANA = "8474498", "GESTOR DA UNIDADE DE ENSINO - INSTITUTO FEDERAL DE SERGIPE - CAMPUS ITABAIANA"
    CAMPUS_LAGARTO = "8474499", "GESTOR DA UNIDADE DE ENSINO - INSTITUTO FEDERAL DE SERGIPE - CAMPUS LAGARTO"
    CAMPUS_NOSSA_SENHORA_GLORIA = "8474501", "GESTOR DA UNIDADE DE ENSINO - INSTITUTO FEDERAL DE SERGIPE - CAMPUS NOSSA SENHORA DA GLÓRIA"
    CAMPUS_SAO_CRISTOVAO = "8474504", "GESTOR DA UNIDADE DE ENSINO - INSTITUTO FEDERAL DE SERGIPE - CAMPUS SÃO CRISTÓVÃO"
    CAMPUS_NOSSA_SENHORA_SOCORRO = "8474507", "GESTOR DA UNIDADE DE ENSINO - INSTITUTO FEDERAL DE SERGIPE CAMPUS NOSSA SENHORA DO SOCORRO"
    CAMPUS_POCO_REDONDO = "8474510", "GESTOR DA UNIDADE DE ENSINO - INSTITUTO FEDERAL DE SERGIPE CAMPUS POÇO REDONDO"
    CAMPUS_PROPRIA = "8474514", "GESTOR DA UNIDADE DE ENSINO - INSTITUTO FEDERAL DE SERGIPE CAMPUS PROPRIÁ"
    CAMPUS_TOBIAS_BARRETO = "8474516", "GESTOR DA UNIDADE DE ENSINO - INSTITUTO FEDERAL DE SERGIPE CAMPUS TOBIAS BARRETO"


class TipoCursoChoices(TextChoices):
    NAOINFORMADO = "", "Selecione..."
    FORMACAO_INICIAL = "1", "FORMAÇÃO INICIAL"
    FORMACAO_CONTINUADA = "2", "FORMAÇÃO CONTINUADA"
    TECNICO = "3", "TÉCNICO"
    TECNOLOGIA = "4", "TECNOLOGIA"
    BACHARELADO = "5", "BACHARELADO"
    LICENCIATURA = "6", "LICENCIATURA"
    ESPECIALIZACAO_LATO_SENSU = "7", "ESPECIALIZAÇÃO (LATO SENSU)"
    MESTRADO = "8", "MESTRADO"
    DOUTORADO = "9", "DOUTORADO"
    ENSINO_MEDIO = "10", "ENSINO MÉDIO"
    MESTRADO_PROFISSIONAL = "11", "MESTRADO PROFISSIONAL"
    APERFEICOAMENTO = "17", "APERFEIÇOAMENTO"
    LATO_SENSU = "18", "LATO SENSU"
    STRICTO_SENSU = "19", "STRICTO SENSU"
    ESPECIALIZACAO_TECNICA = "16", "ESPECIALIZAÇÃO TÉCNICA"
