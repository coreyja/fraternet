from main.models import Brother, Profile
from rush.models import Rushie


def is_brother(profile):
    return Brother.objects.filter(id=profile.id).exists()

def is_rushie(profile):
    return Rushie.objects.filter(id=profile.id).exists()