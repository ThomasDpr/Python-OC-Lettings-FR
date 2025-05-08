"""
Ce fichier définit les patterns d'URL pour l'application Profiles.
Il inclut les routes pour la liste des profils et les détails de chaque profil.
"""

from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
