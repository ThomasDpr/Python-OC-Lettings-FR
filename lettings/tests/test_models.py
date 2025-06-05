"""Tests pour les modèles de l'application lettings."""

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from lettings.models import Address, Letting
from utils.wrapper_print_message import print_test_message


class TestAddressModel(TestCase):
    """Tests pour le modèle Address."""

    @print_test_message("Création d'une adresse avec des données valides")
    def test_address_creation(self):
        """✅ Test fonctionnel : vérifie la création correcte d'une adresse complète."""
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
        self.assertEqual(address.number, 123)
        self.assertEqual(address.street, "Test Street")
        self.assertEqual(address.city, "Test City")
        self.assertEqual(address.state, "TC")
        self.assertEqual(address.zip_code, 12345)
        self.assertEqual(address.country_iso_code, "TST")

    @print_test_message("Validation du champ number - valeurs valides")
    def test_address_number_valid_values(self):
        """
        🔍 Test de validateur :
            - vérifie que number accepte les valeurs dans la plage autorisée.
        """

        address = Address.objects.create(
            number=1,
            street="Test Street",
            city="Test City",
            state="TC",
            zip_code=12345,
            country_iso_code="TST"
        )
        address.full_clean()
        address.number = 9999
        address.full_clean()

    @print_test_message("Validation du champ number - valeurs invalides")
    def test_address_number_invalid_values(self):
        """🔍 + 💥 Test mixte : vérifie les erreurs de validation et contraintes BDD sur number."""
        with self.assertRaises(IntegrityError):
            Address.objects.create(
                number=-1,
                street="Test Street",
                city="Test City",
                state="TC",
                zip_code=12345,
                country_iso_code="TST"
            )
        with self.assertRaises(ValidationError):
            address = Address(
                number=10000,
                street="Test Street",
                city="Test City",
                state="TC",
                zip_code=12345,
                country_iso_code="TST"
            )
            address.full_clean()

    @print_test_message("Validation du champ street")
    def test_address_street_validation(self):
        """🔍 Test de validateur : vérifie la longueur max et présence du champ street."""
        long_street = "A" * 64
        address = Address.objects.create(
            number=123,
            street=long_street,
            city="Test City",
            state="TC",
            zip_code=12345,
            country_iso_code="TST"
        )
        address.full_clean()

        with self.assertRaises(ValidationError):
            address = Address(
                number=123,
                street="A" * 65,
                city="Test City",
                state="TC",
                zip_code=12345,
                country_iso_code="TST"
            )
            address.full_clean()

        with self.assertRaises(ValidationError):
            address = Address(
                number=123,
                street="",
                city="Test City",
                state="TC",
                zip_code=12345,
                country_iso_code="TST"
            )
            address.full_clean()

    @print_test_message("Validation du champ city")
    def test_address_city_validation(self):
        """🔍 Test de validateur : vérifie la longueur max et présence du champ city."""
        long_city = "B" * 64
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city=long_city,
            state="TC",
            zip_code=12345,
            country_iso_code="TST"
        )
        address.full_clean()

        with self.assertRaises(ValidationError):
            address = Address(
                number=123,
                street="Test Street",
                city="B" * 65,
                state="TC",
                zip_code=12345,
                country_iso_code="TST"
            )
            address.full_clean()

        with self.assertRaises(ValidationError):
            address = Address(
                number=123,
                street="Test Street",
                city="",
                state="TC",
                zip_code=12345,
                country_iso_code="TST"
            )
            address.full_clean()

    @print_test_message("Validation du champ state")
    def test_address_state_validation(self):
        """🔍 Test de validateur : vérifie la longueur exacte (2 caractères) du champ state."""
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="CA",
            zip_code=12345,
            country_iso_code="TST"
        )
        address.full_clean()

        with self.assertRaises(ValidationError):
            address = Address(
                number=123,
                street="Test Street",
                city="Test City",
                state="C",
                zip_code=12345,
                country_iso_code="TST"
            )
            address.full_clean()

        with self.assertRaises(ValidationError):
            address = Address(
                number=123,
                street="Test Street",
                city="Test City",
                state="CAL",
                zip_code=12345,
                country_iso_code="TST"
            )
            address.full_clean()

        with self.assertRaises(ValidationError):
            address = Address(
                number=123,
                street="Test Street",
                city="Test City",
                state="",
                zip_code=12345,
                country_iso_code="TST"
            )
            address.full_clean()

    @print_test_message("Validation du champ zip_code")
    def test_address_zip_code_validation(self):
        """
        🔍 + 💥 Test mixte :
        - vérifie la plage valide (validator)
        - vérifie les valeurs interdites (BDD) du zip_code.
        """
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TC",
            zip_code=1,
            country_iso_code="TST"
        )
        address.full_clean()

        address.zip_code = 99999
        address.full_clean()

        with self.assertRaises(ValidationError):
            address = Address(
                number=123,
                street="Test Street",
                city="Test City",
                state="TC",
                zip_code=100000,
                country_iso_code="TST"
            )
            address.full_clean()

        with self.assertRaises(IntegrityError):
            Address.objects.create(
                number=123,
                street="Test Street",
                city="Test City",
                state="TC",
                zip_code=-1,
                country_iso_code="TST"
            )

    @print_test_message("Validation du champ country_iso_code")
    def test_address_country_iso_code_validation(self):
        """
        🔍 Test de validateur :
        - vérifie la longueur exacte = 3 caractères du champ country_iso_code.
        """
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TC",
            zip_code=12345,
            country_iso_code="USA"
        )
        address.full_clean()

        with self.assertRaises(ValidationError):
            Address(
                number=123,
                street="Test Street",
                city="Test City",
                state="TC",
                zip_code=12345,
                country_iso_code="U"
            ).full_clean()

        with self.assertRaises(ValidationError):
            Address(
                number=123,
                street="Test Street",
                city="Test City",
                state="TC",
                zip_code=12345,
                country_iso_code="US"
            ).full_clean()

        with self.assertRaises(ValidationError):
            Address(
                number=123,
                street="Test Street",
                city="Test City",
                state="TC",
                zip_code=12345,
                country_iso_code="USAA"
            ).full_clean()

        with self.assertRaises(ValidationError):
            Address(
                number=123,
                street="Test Street",
                city="Test City",
                state="TC",
                zip_code=12345,
                country_iso_code=""
            ).full_clean()

    @print_test_message("Test de la méthode __str__")
    def test_address_str_method(self):
        """
        ✅ Test fonctionnel :
            - vérifie le rendu de __str__ avec des caractères simples et spéciaux.
        """
        address = Address.objects.create(
            number=456,
            street="Main Avenue",
            city="Test City",
            state="TC",
            zip_code=54321,
            country_iso_code="TST"
        )
        self.assertEqual(str(address), "456 Main Avenue")

        address_special = Address.objects.create(
            number=789,
            street="Rue de l'Église",
            city="Paris",
            state="IL",
            zip_code=75001,
            country_iso_code="FRA"
        )
        self.assertEqual(str(address_special), "789 Rue de l'Église")

    @print_test_message("Test des métadonnées du modèle")
    def test_address_meta(self):
        """✅ Test fonctionnel : vérifie les verbose_name et verbose_name_plural."""
        self.assertEqual(Address._meta.verbose_name, "Address")
        self.assertEqual(Address._meta.verbose_name_plural, "Addresses")

    @print_test_message("Test de contraintes d'intégrité")
    def test_address_integrity_constraints(self):
        """💥 Test de contrainte BDD : vérifie que tous les champs sont requis."""
        with self.assertRaises((ValidationError, IntegrityError)):
            Address.objects.create(
                street="Test Street",
                city="Test City",
                state="TC",
                zip_code=12345,
                country_iso_code="TST"
            )

    @print_test_message("Test avec des cas limites")
    def test_address_edge_cases(self):
        """✅ + 🔍 Test mixte : espaces autour des champs, caractères Unicode."""
        address = Address.objects.create(
            number=123,
            street=" Test Street ",
            city=" Test City ",
            state="TC",
            zip_code=12345,
            country_iso_code="TST"
        )
        self.assertEqual(address.street, " Test Street ")
        self.assertEqual(address.city, " Test City ")

        address_unicode = Address.objects.create(
            number=123,
            street="Tëst Strëët",
            city="Tëst Cïty",
            state="TC",
            zip_code=12345,
            country_iso_code="TST"
        )
        address_unicode.full_clean()

    @print_test_message("Test de performance et de requêtes")
    def test_address_queries(self):
        """✅ Test fonctionnel : vérifie les filtres et le tri sur le modèle Address."""
        # Nombre d'adresses à créer
        nb = 10

        # Créer plusieurs adresses avec des numéros progressifs
        addresses = []
        for i in range(nb):
            address = Address.objects.create(
                number=100 + i,
                street=f"Street {i}",
                city=f"City {i}",
                state="TC",
                zip_code=10000 + i,
                country_iso_code="TST"
            )
            addresses.append(address)

        # Test de filtrage sur la ville
        filtered_addresses = Address.objects.filter(city="City 2")
        self.assertEqual(filtered_addresses.count(), 1)
        self.assertEqual(filtered_addresses.first().number, 102)

        # Test de tri croissant par number
        sorted_addresses = Address.objects.order_by("number")
        self.assertEqual(sorted_addresses.first().number, 100)
        self.assertEqual(sorted_addresses.last().number, 100 + nb - 1)

    @print_test_message("Test de modification d'adresse")
    def test_address_update(self):
        """✅ Test fonctionnel :
            - vérifie que les modifications d'une instance sont bien sauvegardées en base.
        """
        address = Address.objects.create(
            number=123,
            street="Old Street",
            city="Old City",
            state="OC",
            zip_code=12345,
            country_iso_code="OLD"
        )

        # Modifier l'adresse
        address.street = "New Street"
        address.city = "New City"
        address.save()

        # Vérifier que les modifications ont été sauvegardées
        updated_address = Address.objects.get(pk=address.pk)
        self.assertEqual(updated_address.street, "New Street")
        self.assertEqual(updated_address.city, "New City")
        self.assertEqual(str(updated_address), "123 New Street")

    @print_test_message("Test de suppression d'adresse")
    def test_address_deletion(self):
        """✅ Test fonctionnel :
            - vérifie que la suppression d'une adresse la retire bien de la base.
        """
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TC",
            zip_code=12345,
            country_iso_code="TST"
        )
        address_id = address.id

        # Supprimer l'adresse
        address.delete()

        # Vérifier que l'adresse a bien été supprimée
        self.assertEqual(Address.objects.filter(id=address_id).count(), 0)
        with self.assertRaises(Address.DoesNotExist):
            Address.objects.get(id=address_id)


class TestLettingModel(TestCase):
    """Tests pour le modèle Letting."""
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TC",
            zip_code=12345,
            country_iso_code="TST"
        )

    @print_test_message("Création d'une location avec une adresse valide")
    def test_letting_creation(self):
        """✅ Test fonctionnel : création d'un Letting valide et affichage."""
        letting = Letting.objects.create(
            title="Test Letting",
            address=self.address
        )
        self.assertEqual(Letting.objects.count(), 1)
        self.assertEqual(str(letting), "Test Letting")

    @print_test_message("Test qu'une adresse ne peut être utilisée que par une seule location")
    def test_letting_unique_address(self):
        """💥 Test contrainte BDD : une adresse ne peut être liée qu'à un seul Letting."""
        Letting.objects.create(
            title="Letting 1",
            address=self.address
        )
        with self.assertRaises(IntegrityError):
            Letting.objects.create(
                title="Letting 2",
                address=self.address
            )

    @print_test_message("Test de validation du champ title")
    def test_letting_title_validation(self):
        """🔍 Test de validateur : vérifie la longueur maximale du champ title."""
        # Longueur valide
        letting = Letting(
            title="A" * 256,
            address=self.address
        )
        letting.full_clean()

        # Longueur trop grande
        with self.assertRaises(ValidationError):
            Letting(
                title="A" * 257,
                address=self.address
            ).full_clean()

        # Champ vide
        with self.assertRaises(ValidationError):
            Letting(
                title="",
                address=self.address
            ).full_clean()

    @print_test_message("Test d'intégrité : champ address requis")
    def test_letting_address_required(self):
        """💥 Test contrainte BDD : une location ne peut pas exister sans adresse."""
        with self.assertRaises(IntegrityError):
            Letting.objects.create(
                title="Orphan Letting",
                address=None
            )

    @print_test_message("Test de mise à jour du titre")
    def test_letting_update_title(self):
        """✅ Test fonctionnel : modification du champ title."""
        letting = Letting.objects.create(
            title="Old Title",
            address=self.address
        )
        letting.title = "New Title"
        letting.save()

        updated = Letting.objects.get(id=letting.id)
        self.assertEqual(updated.title, "New Title")

    @print_test_message("Suppression d'un letting ne supprime pas l'adresse associée")
    def test_letting_deletion_does_not_delete_address(self):
        """✅ Test fonctionnel : suppression d’un Letting ne supprime PAS l’adresse liée."""
        letting = Letting.objects.create(
            title="Test Letting",
            address=self.address
        )

        # On supprime le letting
        letting.delete()

        # L’adresse doit toujours exister
        self.assertTrue(Address.objects.filter(id=self.address.id).exists())

    @print_test_message("Vérifie les métadonnées du modèle Letting")
    def test_letting_meta(self):
        """✅ Test fonctionnel : vérifie les verbose_name du modèle Letting."""
        self.assertEqual(Letting._meta.verbose_name, "Letting")
        self.assertEqual(Letting._meta.verbose_name_plural, "Lettings")
