from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('translate/', views.translate, name='translate'),
    path('profile/', views.profile, name='profile'),
    path('mylist/', views.mylist, name='mylist'),
    path('theme/<int:pk>', views.theme_details, name='theme-detail'),
    path('theme/<int:pk>/word/<int:key>', views.learn_words, name='learn_words'),
    path('complete/', views.learn_complete, name='complete'),

    path('add_card/<int:pk>', views.add_card, name='add_card'),
    path('delete_card/<int:pk>/', views.delete_card, name='delete_card'),
]
