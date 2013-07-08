from django.db import models
from django.conf import settings

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):

    def save(self, *args, **kwargs):
        self.email = self.username + '@' + settings.FRATERNET_EMAIL_DOMAIN




class Brother(Profile):
    pass