import datetime

from django.db import models


class LateRecord(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    date = models.DateTimeField('date added')
    expires = models.DateTimeField('date expires')
    type = models.CharField(max_length=5)
    schedule = models.CharField(max_length=7)
    diet = models.CharField(max_length=2)
    glutenfree = models.BooleanField()
    nonuts = models.BooleanField()
    nopeanuts = models.BooleanField()

    def __unicode__(self):
        return u'%s %s %s %s %s %i %i %i' % (self.name, self.email, self.type, self.schedule, self.diet, self.glutenfree, self.nonuts, self.nopeanuts)

    def is_active_today(self):
        if self.schedule == 'today':
	    return self.date == datetime.date.today()
        else:
            return self.date == datetime.date.today()
