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

    def all_bro_percentages(self):
        bro_count = Brother.objects.all().count()

        yes = self.votes_yes().count()
        no = self.votes_no().count()
        na = bro_count - yes - no

        yes_per = (yes/(1.0*bro_count))*100.0
        no_per = (no/(1.0*bro_count))*100.0
        na_per = (na/(1.0*bro_count))*100.0

        return yes_per, no_per, na_per

class Vote(models.Model):

    poll = models.ForeignKey(Poll, related_name='votes', null=True, blank=True)

    brother = models.ForeignKey(Brother, related_name='votes_made')

    VOTE_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    vote = models.CharField(max_length=1, choices=VOTE_CHOICES, default='N')