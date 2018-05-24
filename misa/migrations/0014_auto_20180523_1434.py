# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misa', '0013_auto_20180523_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chromatographytype',
            name='ontologyterm',
            field=models.ManyToManyField(to='misa.OntologyTerm'),
        ),
        migrations.RemoveField(
            model_name='measurementtechnique',
            name='ontologyterm',
        ),
        migrations.AddField(
            model_name='measurementtechnique',
            name='ontologyterm',
            field=models.ManyToManyField(to='misa.OntologyTerm'),
        ),
    ]
