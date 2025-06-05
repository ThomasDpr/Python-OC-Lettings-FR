from django.test import TestCase
from django.urls import resolve, reverse

from profiles.views import index, profile


class ProfileUrlsTest(TestCase):
    """Tests pour les URLs de l'application profiles."""

    def test_profiles_index_url(self):
        """Test de l'URL index des profils."""
        url = reverse('profiles:index')
        self.assertEqual(url, '/profiles/')
        self.assertEqual(resolve(url).func, index)

    def test_profile_detail_url(self):
        """Test de l'URL détail d'un profil."""
        url = reverse('profiles:profile', args=['testuser'])
        self.assertEqual(url, '/profiles/testuser/')
        self.assertEqual(resolve(url).func, profile)
