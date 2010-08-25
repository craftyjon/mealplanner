import datetime

from django.db import models

class LateRecord(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    date = models.DateTimeField('date added')
    expires = models.DateTimeField('date expires')
    type = models.CharField(max_length=5)
    schedule = models.CharField(max_length=7)
    diet = models.CharField(max_length=2)
    glutenfree = models.BooleanField()
    nonuts = models.BooleanField()
    nopeanuts = models.BooleanField()

    def __unicode__(self):
        return u'[%d - created %s, expires %s] %s (%s) - %s - %s - %s, glutenfree=%i, nonuts=%i, nopeanuts=%i' % (self.id, self.date.strftime("%a, %b %d"), self.expires.strftime("%a, %b %d"), self.name, self.email, self.type, self.schedule, self.diet, self.glutenfree, self.nonuts, self.nopeanuts)

    def is_active_today(self):
        if self.schedule == 'today':
	    return self.date == datetime.date.today()
        else:
            return self.date == datetime.date.today()
