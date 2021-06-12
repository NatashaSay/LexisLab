from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Words, Themes
from .serializers import WordSerializer, ThemeSerializer


class WordView(APIView):
    def get(self, request):
        words = Words.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response({"words": serializer.data})


class ThemeView(APIView):
    def get(self, request):
        themes = Themes.objects.all()
        serializer = ThemeSerializer(themes, many=True)
        return Response({"themes": serializer.data})


def main_app(request):
    return render(request, 'main_app.html')