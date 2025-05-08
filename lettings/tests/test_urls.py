"""Tests pour les URLs de l'application lettings."""
from django.test import TestCase
from django.urls import resolve, reverse

from lettings.views import index, letting


class TestLettingsUrls(TestCase):
    """Tests pour les URLs de l'application lettings."""

    def test_index_url_resolves(self):
        """Test que l'URL 'lettings:index' résout vers la bonne vue."""
        path = reverse('lettings:index')
        self.assertEqual(path, '/lettings/')
        resolver = resolve(path)
        self.assertEqual(resolver.func, index)
        self.assertEqual(resolver.namespace, 'lettings')
        self.assertEqual(resolver.url_name, 'index')

    def test_letting_detail_url_resolves(self):
        """Test que l'URL 'lettings:letting' résout vers la bonne vue."""
        path = reverse('lettings:letting', kwargs={'letting_id': 1})
        self.assertEqual(path, '/lettings/1/')
        resolver = resolve(path)
        self.assertEqual(resolver.func, letting)
        self.assertEqual(resolver.namespace, 'lettings')
        self.assertEqual(resolver.url_name, 'letting')

    def test_letting_detail_url_with_different_id(self):
        """Test que l'URL 'lettings:letting' fonctionne avec différents IDs."""
        path = reverse('lettings:letting', kwargs={'letting_id': 999})
        self.assertEqual(path, '/lettings/999/')
