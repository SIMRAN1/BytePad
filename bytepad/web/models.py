from __future__ import unicode_literals

from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Session(models.Model):
    year = models.CharField(max_length=255)

    def __unicode__(self):
        return self.year


class Paper(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField()
    exam = models.ForeignKey('Exam')
    session = models.ForeignKey('Session')

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.name, self.exam, self.session)


class LastUpdate(models.Model):
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return str(self.timestamp)
