import sentry_sdk
from django.shortcuts import get_object_or_404, render

from .models import Letting


def index(request):
    """
    Affiche la page d'accueil des locations.

    Récupère la liste de toutes les locations disponibles et les affiche
    dans un template.

    Args:
        request: La requête HTTP reçue

    Returns:
        HttpResponse: La page HTML rendue avec la liste des locations
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    """
    Affiche les détails d'une location spécifique.

    Récupère les informations de la location correspondante et les affiche
    dans un template.

    Args:
        request: La requête HTTP reçue
        letting_id: L'identifiant de la location à afficher

    Returns:
        HttpResponse: La page HTML rendue avec les détails de la location
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'letting.html', context)
    except Exception as e:
        # Capturer explicitement l'exception pour plus de contexte
        sentry_sdk.capture_exception(e)
        raise  # Relancer l'exception pour le comportement normal de Django