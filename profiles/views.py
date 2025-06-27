from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def profiles_index(request):

    """
    Vue de la page d'index des profils.

    Affiche la liste de tous les profils utilisateurs disponibles dans le système.
    Les profils sont triés par nom d'utilisateur par défaut.

    Args:
        request (HttpRequest): Objet de requête Django contenant les métadonnées
                              de la requête HTTP.

    Examples:
        >>> # Accès via URL: /profiles/
        >>> response = profiles_index(request)
        >>> assert response.status_code == 200
        >>> assert 'profiles_list' in response.context

    Note:
        Cette vue affiche tous les profils actifs. Les utilisateurs inactifs
        sont inclus dans la liste mais peuvent être filtrés côté template.
    """

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis  dolor id facilisis ,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique


def profile(request, username):

    """
    Vue de détail d'un profil utilisateur spécifique.

    Affiche les informations détaillées d'un profil identifié par le nom
    d'utilisateur, incluant les données personnelles et la ville favorite.

    Args:
        request (HttpRequest): Objet de requête Django contenant les métadonnées
                              de la requête HTTP.
        username (str): Nom d'utilisateur unique identifiant le profil à afficher.

    Returns:
        HttpResponse: Réponse HTTP avec le template rendu contenant les détails
                     du profil.

    Examples:
        >>> # Accès via URL: /profiles/john/
        >>> response = profile(request, 'john')
        >>> assert response.status_code == 200
        >>> assert 'profile' in response.context
        >>> assert response.context['profile'].user.username == 'john'

    Note:
        La recherche se fait sur le nom d'utilisateur exact (sensible à la casse).
        Le profil inclut automatiquement les informations de l'utilisateur Django
        associé grâce à la relation OneToOne.
    """

    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
