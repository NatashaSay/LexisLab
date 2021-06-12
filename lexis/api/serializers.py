from rest_framework import serializers

class WordSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()


class ThemeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()