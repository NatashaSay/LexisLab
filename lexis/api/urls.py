from django.urls import path
from . import views

urlpatterns = [
    path('words/', views.WordView.as_view(), name='get-words'),
    path('themes/', views.ThemeView.as_view(), name='get-themes'),
    path('app', views.main_app, name='main-app'),
]
