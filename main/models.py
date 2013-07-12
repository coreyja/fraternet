from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import AbstractUser, BaseUserManager


class ProfileManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        now = timezone.now()

        user = self.model(username=username,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        u = self.create_user(username, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save()
        return u


class Profile(AbstractUser):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    objects = ProfileManager()

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        self.email = self.username + '@' + settings.FRATERNET_EMAIL_DOMAIN


class Brother(Profile):
    class Meta:
        verbose_name = "Brother"
        verbose_name_plural = "Brothers"
    pass