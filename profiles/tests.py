import pytest
from django.urls import reverse
from django.test import Client
from .models import Profile


@pytest.mark.django_db
def test_profiles_index_view():
    """Test que la vue profiles_index retourne un statut 200 et contient les profils."""
    # Création du client de test
    client = Client()

    # Accès à la vue
    url = reverse('profiles_index')
    response = client.get(url)

    # Vérifications
    assert response.status_code == 200
    assert 'profiles_list' in response.context


@pytest.mark.django_db
def test_profile_detail_view():
    """Test profile retourne un statut 200 et le bon profil."""
    # Création d'un utilisateur et d'un profil de test
    from django.contrib.auth.models import User

    user = User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="testpassword"
    )

    profile = Profile.objects.create(
        user=user,
        favorite_city="Test City"
    )

    # Création du client de test
    client = Client()

    # Accès à la vue avec l'utilisateur créé
    url = reverse('profile', kwargs={'username': "testuser"})
    response = client.get(url)

    # Vérifications
    assert profile == response.context['profile']
    assert response.status_code == 200
    assert 'profile' in response.context
    assert response.context['profile'].user.username == "testuser"
