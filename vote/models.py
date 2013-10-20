from django.db import models

from rush.models import Rushie
from main.models import Brother


class Poll(models.Model):

    rushee = models.ForeignKey(Rushie, related_name='polls')

    open = models.BooleanField(default=True)

    def votes_yes(self):
        return self.votes.filter(vote='Y')

    def votes_no(self):
        return self.votes.filter(vote='N')

    def yes_percent(self):
        return (self.votes_yes().count() / (self.votes.count()*1.0))*100.0

    def no_percent(self):
        return (self.votes_no().count() / (self.votes.count()*1.0))*100.0

class Vote(models.Model):

    poll = models.ForeignKey(Poll, related_name='votes')

    brother = models.ForeignKey(Brother, related_name='votes_made')

    VOTE_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    vote = models.CharField(max_length=1, choices=VOTE_CHOICES, default='N')