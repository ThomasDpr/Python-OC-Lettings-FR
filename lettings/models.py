"""
Ce module contient les modèles pour l'application Lettings.
Il définit les TABLES :
    - Address : représente les adresses.
    - Letting : représente les locations disponibles.
"""

from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Représente une adresse physique pour une location.
    Chaque adresse est composée d'un numéro, rue, ville, état, code postal et pays.
    Une adresse peut être associée à une seule location via une relation OneToOne.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """
        Ici on gère l'erreur de pluralisation pour l'espace admin.
        """
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de l'adresse.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Représente une location disponible.
    Chaque location est associée à une adresse unique.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        """
        Ici on gère l'erreur de pluralisation pour l'espace admin.
        """
        verbose_name = "Letting"
        verbose_name_plural = "Lettings"

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de la location.
        """
        return self.title
