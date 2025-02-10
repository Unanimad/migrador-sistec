from rest_framework import serializers

class IDNameSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
