from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import AbstractUser, BaseUserManager
from sortedm2m.fields import SortedManyToManyField


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


class BrotherManager(ProfileManager):
    pass


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

    phone = models.CharField(max_length=10, blank=True, null=True)
    grad_year = models.IntegerField(blank=True, null=True)

    from django import forms
    majors = SortedManyToManyField('main.Major', related_name='brothers', blank=True, null=True)

    objects = BrotherManager()

    def name(self):
        return self.first_name + ' ' + self.last_name

    def list_majors(self):
        list = ''

        for major in self.majors.all():
            list += str(major) + ', '

        if list == '': return '';

        #Remove the last space and comma
        return list[:-2]

    def list_majors_abbrev(self):
        list = ''

        for major in self.majors.all():
            list += str(major.abbrev) + ', '

        if list == '': return '';

        #Remove the last space and comma
        return list[:-2]

    def can_edit_brother(self,id):
        return self.id == id or self.has_perm('main.change_brother')


class Major(models.Model):

    title = models.CharField(max_length=20, blank=False, null=False)
    abbrev = models.CharField(max_length=5)

    def __unicode__(self):
        return self.title
