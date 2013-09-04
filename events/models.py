from django.db import models
from django.conf import settings
from django.utils import timezone


class Event(models.Model):

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
