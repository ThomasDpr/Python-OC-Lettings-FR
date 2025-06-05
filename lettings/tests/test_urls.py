"""Tests pour les URLs et les vues de l'application lettings."""

from django.test import TestCase
from django.urls import resolve, reverse

from lettings.models import Address, Letting
from lettings.views import index, letting
from utils.wrapper_print_message import print_test_message


class TestLettingsUrls(TestCase):
    """Tests unitaires et fonctionnels pour les URLs et vues de l'app lettings."""

    def setUp(self):
        """Création d'une adresse et d'une location commune à tous les tests."""
        self.address = Address.objects.create(
            number=42,
            street="Rue de Paris",
            city="Paris",
            state="PA",
            zip_code=75000,
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(
            title="Paris Center",
            address=self.address
        )

    # --- TESTS UNITAIRES DES URLS ---

    @print_test_message("Test que l'URL 'lettings:index' est correctement résolue")
    def test_index_url_resolves(self):
        path = reverse('lettings:index')
        self.assertEqual(path, '/lettings/')
        resolver = resolve(path)
        self.assertEqual(resolver.func, index)
        self.assertEqual(resolver.namespace, 'lettings')
        self.assertEqual(resolver.url_name, 'index')

    @print_test_message("Test que l'URL 'lettings:letting' est correctement résolue")
    def test_letting_detail_url_resolves(self):
        path = reverse('lettings:letting', kwargs={'letting_id': self.letting.id})
        self.assertEqual(path, f'/lettings/{self.letting.id}/')
        resolver = resolve(path)
        self.assertEqual(resolver.func, letting)
        self.assertEqual(resolver.namespace, 'lettings')
        self.assertEqual(resolver.url_name, 'letting')

    @print_test_message("Test que l'URL letting accepte différents IDs")
    def test_letting_detail_url_with_different_id(self):
        path = reverse('lettings:letting', kwargs={'letting_id': 999})
        self.assertEqual(path, '/lettings/999/')

    # --- TESTS FONCTIONNELS DE RÉPONSE HTTP ET RENDU ---

    @print_test_message("Test que la page index retourne une réponse HTTP 200")
    def test_index_view_http_response(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)

    @print_test_message("Test que la page letting retourne une réponse HTTP 200")
    def test_letting_view_http_response(self):
        response = self.client.get(
            reverse('lettings:letting', kwargs={'letting_id': self.letting.id}),
            data={'letting_id': self.letting.id}
        )
        self.assertEqual(response.status_code, 200)

    @print_test_message("Test que la vue letting retourne 404 si l'ID est introuvable")
    def test_letting_view_404_when_not_found(self):
        response = self.client.get(reverse('lettings:letting', kwargs={'letting_id': 9999}))
        self.assertEqual(response.status_code, 404)

    # --- TESTS DU CONTENU HTML ---

    @print_test_message("Test du contenu HTML de la page index")
    def test_index_page_content(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, "Paris Center")
        self.assertContains(response, f'href="/lettings/{self.letting.id}/"')

    @print_test_message("Test du contenu HTML de la page letting")
    def test_letting_page_content(self):
        response = self.client.get(
            reverse('lettings:letting', kwargs={'letting_id': self.letting.id}),
            data={'letting_id': self.letting.id}
        )
        self.assertContains(response, "Paris Center")
        self.assertContains(response, "42 Rue de Paris")
        self.assertContains(response, "Paris, PA 75000")
        self.assertContains(response, "FRA")
