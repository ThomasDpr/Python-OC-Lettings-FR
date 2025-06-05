from django.contrib.auth.models import User
from django.test import TestCase

from profiles.models import Profile


class ProfileModelTest(TestCase):
    """Tests pour le modèle Profile."""

    def setUp(self):
        """Création d'un utilisateur et profil pour les tests."""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Paris'
        )

    def test_profile_creation(self):
        """Test de création d'un profil."""
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.favorite_city, 'Paris')

    def test_profile_str_method(self):
        """Test de la méthode __str__ du profil."""
        self.assertEqual(str(self.profile), 'testuser')

    def test_profile_user_relationship(self):
        """Test de la relation OneToOne avec User."""
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.user.user_profile, self.profile)
