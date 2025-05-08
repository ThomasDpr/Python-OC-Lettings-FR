"""
Ce fichier définit les patterns d'URL principaux pour l'application.
Il inclut les routes pour les applications lettings et profiles.

Il gère également les erreurs 404 et 500.
"""

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    # Pour sentry pour tester la configuration
    path('sentry-debug/', views.trigger_error),
]

handler404 = 'oc_lettings_site.views.handler404'
handler500 = 'oc_lettings_site.views.handler500'
