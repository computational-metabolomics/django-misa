# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misa', '0006_auto_20180523_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='public_release_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='submission_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
