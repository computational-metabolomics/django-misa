# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misa', '0009_auto_20180523_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='organismpart',
            name='name',
            field=models.TextField(blank=True),
        ),
    ]
