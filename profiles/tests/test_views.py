from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from profiles.models import Profile


class ProfileViewsTest(TestCase):
    """Tests pour les vues de l'application profiles."""
    def setUp(self):
        """Configuration pour les tests."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Paris'
        )

    def test_profiles_index_view(self):
        """Test de la vue index des profils."""
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_profile_detail_view(self):
        """Test de la vue détail d'un profil."""
        response = self.client.get(
            reverse('profiles:profile', args=[self.user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, 'Paris')
