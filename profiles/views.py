"""
Ce module contient les vues pour l'application Profiles.
Il définit les vues pour la liste des profils et les détails de chaque profil.
"""

from django.shortcuts import render

from .models import Profile


def index(request):
    """
    Affiche la page d'accueil des profils.

    Récupère la liste de tous les profils et les affiche
    dans un template.

    Args:
        request: La requête HTTP reçue

    Returns:
        HttpResponse: La page HTML rendue avec la liste des profils
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


def profile(request, username):
    """
    Affiche les détails d'un profil spécifique.

    Récupère les informations du profil correspondant et les affiche
    dans un template.

    Args:
        request: La requête HTTP reçue
        username: Le nom d'utilisateur du profil à afficher

    Returns:
        HttpResponse: La page HTML rendue avec les détails du profil
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
