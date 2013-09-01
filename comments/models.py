from django.db import models
from datetime import datetime

from main.models import Profile

class Comment(models.Model):

    timestamp = models.DateTimeField(default=datetime.now)
    comment = models.TextField()

    created_by = models.ForeignKey(Profile, related_name='comments_made')

    def __unicode__(self):
        return self.comment