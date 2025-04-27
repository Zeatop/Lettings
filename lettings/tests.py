import pytest
from django.urls import reverse
from django.test import Client
from .models import Letting, Address


@pytest.mark.django_db
def test_lettings_index_view():
    """Test que la vue lettings_index retourne un statut 200 et contient la liste des locations."""
    # Création du client de test
    client = Client()

    # Accès à la vue
    url = reverse('lettings_index')
    response = client.get(url)

    # Vérifications
    assert response.status_code == 200
    assert 'lettings_list' in response.context


@pytest.mark.django_db
def test_letting_detail_view():
    """Test que la vue letting retourne un statut 200 et les bonnes informations de location."""
    # Création d'une adresse et d'une location de test
    address = Address.objects.create(
        number=123,
        street="Test Street",
        city="Test City",
        state="CA",
        zip_code=12345,
        country_iso_code="USA"
    )

    letting = Letting.objects.create(
        title="Test Letting",
        address=address
    )

    # Création du client de test
    client = Client()

    # Accès à la vue
    url = reverse('letting', kwargs={'letting_id': letting.id})
    response = client.get(url)

    # Vérifications
    assert response.status_code == 200
    assert 'title' in response.context
    assert 'address' in response.context
    assert response.context['title'] == "Test Letting"
    assert response.context['address'] == address
