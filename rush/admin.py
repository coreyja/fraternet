from django.contrib import admin
from .models import Rushie, RushieComment, ClosedRush, RushEvent

admin.site.register(Rushie)

admin.site.register(RushieComment)

admin.site.register(ClosedRush)
admin.site.register(RushEvent)