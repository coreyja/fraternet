from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import AbstractUser, BaseUserManager
from sortedm2m.fields import SortedManyToManyField

from main.models import ProfileManager, Profile

from comments.models import Comment

class RushieManager(ProfileManager):
    pass


class Rushie(Profile):
    class Meta:
        verbose_name = "Rushie"
        verbose_name_plural = "Rushies"

    phone = models.CharField(max_length=10, blank=True, null=True)
    grad_year = models.IntegerField(blank=True, null=True)

    majors = SortedManyToManyField('main.Major', related_name='rushies', blank=True, null=True)

    objects = RushieManager()

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


class RushieComment(Comment):

    commented_on = models.ForeignKey(Rushie, related_name='comments')