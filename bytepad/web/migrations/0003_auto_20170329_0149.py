# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_lastupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='file',
            field=models.FileField(upload_to=web.models.upload_document),
        ),
    ]
