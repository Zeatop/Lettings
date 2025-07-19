from django.shortcuts import render

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis
# enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.


def index(request):

    """
    Vue de la page d'accueil de l'application.

    Cette vue affiche la page d'accueil principale du site Orange County Lettings,
    qui sert de point d'entrée pour naviguer vers les sections profils et locations.
    La page présente un aperçu général de l'application et des liens de navigation
    vers les fonctionnalités principales.

    Args:
        request (HttpRequest): Objet de requête Django contenant les métadonnées
                              de la requête HTTP, les headers, et les informations
                              de session utilisateur.

    URL Pattern:
        Cette vue est associée à l'URL racine '/' du site.

    Examples:
        >>> # Accès via URL: /
        >>> response = index(request)
        >>> assert response.status_code == 200
        >>> assert 'Orange County Lettings' in response.content.decode()
    """

    return render(request, 'index.html')
