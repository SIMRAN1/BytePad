from __future__ import unicode_literals

import os
from uuid import uuid4

from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Session(models.Model):
    year = models.CharField(max_length=255)

    def __unicode__(self):
        return self.year


def upload_document(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join('{}/{}'.format(instance.session, instance.exam), filename)


class Paper(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=upload_document)
    exam = models.ForeignKey('Exam')
    session = models.ForeignKey('Session')

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.name, self.exam, self.session)


class LastUpdate(models.Model):
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return str(self.timestamp)
