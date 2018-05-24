# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('misa', '0004_auto_20180523_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organism',
            name='ontologyterm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='misa.OntologyTerm'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organismpart',
            name='ontologyterm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='misa.OntologyTerm'),
            preserve_default=False,
        ),
    ]
