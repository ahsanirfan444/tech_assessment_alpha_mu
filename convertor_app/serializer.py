from rest_framework import serializers

class ConvertToNumberSerializer(serializers.Serializer):
    words = serializers.CharField()

class ConvertToWordSerializer(serializers.Serializer):
    number = serializers.IntegerField()