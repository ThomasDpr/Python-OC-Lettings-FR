import os

import django

from lettings.models import Address as NewAddress
from lettings.models import Letting as NewLetting
from oc_lettings_site.models import Address as OldAddress
from oc_lettings_site.models import Letting as OldLetting
from oc_lettings_site.models import Profile as OldProfile
from profiles.models import Profile as NewProfile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
django.setup()


# Migration des adresses
for old_address in OldAddress.objects.all():
    new_address = NewAddress(
        id=old_address.id,
        number=old_address.number,
        street=old_address.street,
        city=old_address.city,
        state=old_address.state,
        zip_code=old_address.zip_code,
        country_iso_code=old_address.country_iso_code
    )
    new_address.save()
    print(f"Adresse migrée: {new_address}")

# Migration des locations
for old_letting in OldLetting.objects.all():
    new_address = NewAddress.objects.get(id=old_letting.address.id)
    new_letting = NewLetting(
        id=old_letting.id,
        title=old_letting.title,
        address=new_address
    )
    new_letting.save()
    print(f"Location migrée: {new_letting}")

# Migration des profils
for old_profile in OldProfile.objects.all():
    new_profile = NewProfile(
        id=old_profile.id,
        user=old_profile.user,
        favorite_city=old_profile.favorite_city
    )
    new_profile.save()
    print(f"Profil migré: {new_profile}")

print("Migration des données terminée avec succès!")
