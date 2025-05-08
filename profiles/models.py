
"""
Ce module contient les modèles pour l'application Profiles.
Il définit les TABLES :
    - Profile : représente les profils des utilisateurs.
"""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Représente le profil d'un utilisateur.
    Chaque profil est associé à un utilisateur unique.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        """
        Ici on gère l'erreur de pluralisation pour l'espace admin.
        """
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """
        Retourne le nom d'utilisateur du profil.
        """
        return self.user.username
