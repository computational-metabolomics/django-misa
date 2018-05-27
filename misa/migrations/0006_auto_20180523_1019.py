# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 10:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('misa', '0005_auto_20180523_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='funding_agency',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='study',
            name='grant_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='study',
            name='public_release_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='study',
            name='study_design_descriptors',
            field=models.ManyToManyField(help_text="Any ontological terms that can describe or 'tag' the study <a target='_blank' href='/misa/search_ontologyterm/'>add</a>.", to='misa.OntologyTerm'),
        ),
        migrations.AddField(
            model_name='study',
            name='submission_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='study',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studyfactor',
            name='value',
            field=models.CharField(blank=True, help_text='If no appropiate ontological term for the value, then add free text here', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='name',
            field=models.CharField(help_text='e.g. the study identifier', max_length=100),
        ),
        migrations.AlterField(
            model_name='studyfactor',
            name='ontologyterm_type',
            field=models.ForeignKey(blank=True, help_text="The type for the value e.g. gene knockout, concentration unit, etc If the ontology term is not available please  <a target='_blank' href='/misa/search_ontologyterm/'>add</a>.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ontologyterm_type', to='misa.OntologyTerm', verbose_name='Ontology Term (type)'),
        ),
        migrations.AlterField(
            model_name='studyfactor',
            name='ontologyterm_value',
            field=models.ForeignKey(blank=True, help_text="The value, e.g. if  wild type, 5 Mol, etc If the ontology term is not available please  <a target='_blank' href='/misa/search_ontologyterm/'>add</a>.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ontologyterm_value', to='misa.OntologyTerm', verbose_name='Ontology Term (type)'),
        ),
    ]