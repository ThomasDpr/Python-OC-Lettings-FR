"""Tests pour les vues de l'application lettings."""
from django.http import Http404
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from lettings.models import Address, Letting
from lettings.views import index, letting


class TestLettingsViews(TestCase):

    """Tests pour les vues de l'application lettings."""
    def setUp(self):
        """Initialisation avant chaque test."""
        self.client = Client()
        self.factory = RequestFactory()
        # Créer une adresse et une location pour les tests
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TC",
            zip_code=12345,
            country_iso_code="TST"
        )
        self.letting = Letting.objects.create(
            title="Test Letting",
            address=self.address
        )

    def test_index_view(self):
        """Test que la vue index retourne une réponse 200 et contient des données correctes."""
        # Test avec Client pour vérifier le rendu complet
        path = reverse('lettings:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")
        # Test direct de la fonction de vue
        request = self.factory.get(path)
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_letting_detail_view(self):
        """Test que la vue de détail d'une location fonctionne correctement."""
        # Test avec Client
        path = reverse('lettings:letting', kwargs={'letting_id': self.letting.id})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")
        self.assertContains(response, "123 Test Street")
        request = self.factory.get(path)
        response = letting(request, letting_id=self.letting.id)
        self.assertEqual(response.status_code, 200)

    def test_letting_detail_view_with_invalid_id(self):
        """Test que la vue de détail avec un ID inexistant génère une erreur."""
        with self.assertRaises(Http404):
            path = reverse('lettings:letting', kwargs={'letting_id': 9999})  # ID qui n'existe pas
            request = self.factory.get(path)
            letting(request, letting_id=9999)
