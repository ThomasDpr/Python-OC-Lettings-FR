"""
Ce module contient les vues pour l'application oc_lettings_site.
Il définit les vues pour la page d'accueil et les gestionnaires d'erreurs.
"""

from django.shortcuts import render


def index(request):
    """
    Affiche la page d'accueil de l'application.
    """
    return render(request, 'index.html')


def handler404(request, exception):
    """
    Gère l'erreur 404 (page non trouvée).
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """
    Gère l'erreur 500 (erreur interne du serveur).
    """
    return render(request, '500.html', status=500)


# Pour sentry pour tester la configuration
def trigger_error(request):
    """Vue de test pour vérifier la configuration de Sentry."""
    division_by_zero = 1 / 0
    return division_by_zero
