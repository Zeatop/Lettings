from django.shortcuts import render
from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus
# orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def lettings_index(request):

    """
    Vue de la page d'index des locations.

    Affiche la liste de toutes les locations disponibles dans le système.

    Args:
        request (HttpRequest): Objet de requête Django contenant les métadonnées
                              de la requête HTTP.

    Returns:
        HttpResponse: Réponse HTTP avec le template rendu contenant la liste
                     des locations.

    Template:
        lettings_index.html

    Context:
        lettings_list (QuerySet): Liste de tous les objets Letting.

    Examples:
        >>> # Accès via URL: /lettings/
        >>> response = lettings_index(request)
        >>> assert response.status_code == 200
    """

    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl.
# Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae efficitur
# lacus justo nec purus. Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit.
# Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis
# ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim,
# ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):

    """
    Vue de détail d'une location spécifique.

    Affiche les informations détaillées d'une location identifiée par son ID,
    incluant le titre et l'adresse complète.

    Args:
        request (HttpRequest): Objet de requête Django contenant les métadonnées
                              de la requête HTTP.
        letting_id (int): Identifiant unique de la location à afficher.

    Returns:
        HttpResponse: Réponse HTTP avec le template rendu contenant les détails
                     de la location.

    Examples:
        >>> # Accès via URL: /lettings/1/
        >>> response = letting(request, 1)
        >>> assert response.status_code == 200
        >>> assert 'title' in response.context
        >>> assert 'address' in response.context
    """

    letting = Letting.objects.get(pk=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)
