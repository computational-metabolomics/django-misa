# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misa', '0014_auto_20180523_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extractiontype',
            name='ontologyterm',
        ),
        migrations.AddField(
            model_name='extractiontype',
            name='ontologyterm',
            field=models.ManyToManyField(to='misa.OntologyTerm'),
        ),
    ]
