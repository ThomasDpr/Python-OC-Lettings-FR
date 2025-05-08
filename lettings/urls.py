"""
Ce fichier définit les patterns d'URL pour l'application Lettings.
Il inclut les routes pour la liste des locations et les détails de chaque location.
"""

from django.urls import path

from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
