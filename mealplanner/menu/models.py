import datetime

from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    diet = models.CharField(max_length=2)
    glutenfree = models.BooleanField()
    nonuts = models.BooleanField()
    nopeanuts = models.BooleanField()

    def __unicode__(self):
        return u'[%d ] %s (%s) - glutenfree=%i, nonuts=%i, nopeanuts=%i' % (self.id, self.name, self.description, self.glutenfree, self.nonuts, self.nopeanuts)
