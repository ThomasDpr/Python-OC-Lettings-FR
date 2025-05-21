"""Tests pour les modèles de l'application lettings."""
import pytest
from django.core.exceptions import ValidationError
from django.test import TestCase

from lettings.models import Address, Letting
from utils.wrapper_print_message import print_test_message


class TestAddressModel(TestCase):
    """Tests pour le modèle Address."""

    @print_test_message("Création d'une adresse")
    def test_address_creation(self):
        """Test la création d'une adresse avec des données valides."""
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TC",
            zip_code=12345,
            country_iso_code="TST"
        )
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(str(address), "123 Test Street")

    @print_test_message("Validation des champs de l'adresse")
    def test_address_validation(self):
        """Test la validation des champs de l'adresse."""
        # Test qu'un code pays trop court provoque une erreur
        address = Address(
            number=123,
            street="Test Street",
            city="Test City",
            state="TC",
            zip_code=12345,
            country_iso_code="T"  # Trop court, devrait être 3 caractères
        )
        with self.assertRaises(ValidationError):
            address.full_clean()


class TestLettingModel(TestCase):
    """Tests pour le modèle Letting."""

    @print_test_message("Création d'une location avec une adresse valide")
    def test_letting_creation(self):
        """Test la création d'une location avec une adresse valide."""
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TC",
            zip_code=12345,
            country_iso_code="TST"
        )
        letting = Letting.objects.create(
            title="Test Letting",
            address=address
        )
        self.assertEqual(Letting.objects.count(), 1)
        self.assertEqual(str(letting), "Test Letting")

    @print_test_message("Test qu'une adresse ne peut être utilisée que par une seule location")
    def test_letting_unique_address(self):
        """Test qu'une adresse ne peut être utilisée que par une seule location."""
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TC",
            zip_code=12345,
            country_iso_code="TST"
        )
        Letting.objects.create(
            title="Test Letting 1",
            address=address
        )
        # Essayer de créer une deuxième location avec la même adresse devrait échouer
        with self.assertRaises(Exception):  # IntegrityError
            Letting.objects.create(
                title="Test Letting 2",
                address=address
            )
