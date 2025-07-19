from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):

    """
    Fonction de test pour Sentry.

    Génère volontairement une erreur de division par zéro pour tester
    l'intégration et la capture d'erreurs par Sentry en développement.

    Args:
        request (HttpRequest): Objet de requête Django.

    Raises:
        ZeroDivisionError: Erreur intentionnelle pour test Sentry.

    URL Pattern:
        /sentry-debug/
    """

    return 1 / 0


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls'))
]

"""
Patterns d'URLs définis :

- '' : Page d'accueil (vue index)
- 'admin/' : Interface d'administration Django
- 'lettings/' : URLs de l'application lettings
- 'profiles/' : URLs de l'application profiles
- 'sentry-debug/' : Endpoint de test pour Sentry (développement uniquement)
"""
