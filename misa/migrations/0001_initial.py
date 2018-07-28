# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import misa.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gfiles', '0001_initial'),
        ('mbrowse', '0002_CUSTOM_IMPORT_DATA'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=40, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AssayDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_field', models.CharField(db_column='code_', max_length=100, validators=[misa.models.validate_workflow_code])),
                ('assay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.Assay')),
            ],
        ),
        migrations.CreateModel(
            name='AssayRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technical_replicate', models.IntegerField(default=1)),
                ('assaydetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.AssayDetail')),
                ('run', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mbrowse.Run')),
            ],
        ),
        migrations.CreateModel(
            name='ChromatographyProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('details', models.CharField(max_length=300)),
                ('chromatographyfrac', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChromatographyProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('uri', models.CharField(blank=True, max_length=200, null=True)),
                ('version', models.CharField(blank=True, max_length=30, null=True)),
                ('code_field', models.CharField(max_length=20, unique=True)),
                ('instrument_name', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChromatographyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=40, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataTransformationProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataTransformationProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('uri', models.CharField(blank=True, max_length=200, null=True)),
                ('version', models.CharField(blank=True, max_length=30, null=True)),
                ('code_field', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExtractionProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('details', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ExtractionProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('uri', models.CharField(blank=True, max_length=200, null=True)),
                ('version', models.CharField(blank=True, max_length=30, null=True)),
                ('code_field', models.CharField(max_length=20, unique=True)),
                ('postextraction', models.CharField(blank=True, max_length=300, null=True)),
                ('derivitisation', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExtractionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=6, unique=True)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(help_text='Investigation description')),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('details', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('uri', models.CharField(blank=True, max_length=200, null=True)),
                ('version', models.CharField(blank=True, max_length=30, null=True)),
                ('code_field', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeasurementTechnique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetaboliteIdentificationProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetaboliteIdentificationProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('uri', models.CharField(blank=True, max_length=200, null=True)),
                ('version', models.CharField(blank=True, max_length=30, null=True)),
                ('code_field', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MISAFile',
            fields=[
                ('genericfile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gfiles.GenericFile')),
                ('investigation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.Investigation')),
            ],
            bases=('gfiles.genericfile',),
        ),
        migrations.CreateModel(
            name='OntologyTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('ontology_id', models.TextField(blank=True, null=True)),
                ('iri', models.TextField(blank=True, null=True)),
                ('obo_id', models.CharField(blank=True, max_length=200, null=True)),
                ('ontology_name', models.CharField(blank=True, max_length=200, null=True)),
                ('ontology_prefix', models.CharField(blank=True, max_length=200, null=True)),
                ('short_form', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('ontologyterm', models.ForeignKey(help_text="If the ontology term is not available, please  <a target='_blank' href='/misa/search_ontologyterm/'>add</a>.", null=True, on_delete=django.db.models.deletion.CASCADE, to='misa.OntologyTerm')),
            ],
        ),
        migrations.CreateModel(
            name='OrganismPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('ontologyterm', models.ForeignKey(help_text="If the ontology term is not available, please  <a target='_blank' href='/misa/search_ontologyterm/'>add</a>.", null=True, on_delete=django.db.models.deletion.CASCADE, to='misa.OntologyTerm')),
            ],
        ),
        migrations.CreateModel(
            name='PolarityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('ontologyterm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='misa.OntologyTerm')),
            ],
            options={
                'verbose_name_plural': 'polarity types',
            },
        ),
        migrations.CreateModel(
            name='SampleCollectionProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SampleCollectionProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('uri', models.CharField(blank=True, max_length=200, null=True)),
                ('version', models.CharField(blank=True, max_length=30, null=True)),
                ('code_field', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SampleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('ontologyterm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='misa.OntologyTerm')),
            ],
        ),
        migrations.CreateModel(
            name='SpeProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('details', models.CharField(max_length=300)),
                ('spefrac', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SpeProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('uri', models.CharField(blank=True, max_length=200, null=True)),
                ('version', models.CharField(blank=True, max_length=30, null=True)),
                ('code_field', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30, unique=True)),
                ('ontologyterm', models.ManyToManyField(to='misa.OntologyTerm')),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Study description')),
                ('dmastudy', models.BooleanField()),
                ('name', models.CharField(help_text='e.g. the study identifier', max_length=100)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('grant_number', models.CharField(blank=True, max_length=100, null=True)),
                ('funding_agency', models.CharField(blank=True, max_length=100, null=True)),
                ('submission_date', models.DateTimeField(blank=True, null=True)),
                ('public_release_date', models.DateTimeField(blank=True, null=True)),
                ('investigation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.Investigation')),
                ('study_design_descriptors', models.ManyToManyField(help_text="Any ontological terms that can describe or 'tag' the study <a target='_blank' href='/misa/search_ontologyterm/'>add</a>.", to='misa.OntologyTerm')),
            ],
        ),
        migrations.CreateModel(
            name='StudyFactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, help_text='If no appropriate ontological term for the value, then add free text here', max_length=100, null=True)),
                ('ontologyterm_type', models.ForeignKey(help_text="The type for the value e.g. gene knockout, concentration unit, etc If the ontology term is not available please  <a target='_blank' href='/misa/search_ontologyterm/'>add</a>.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ontologyterm_type', to='misa.OntologyTerm', verbose_name='Ontology Term (type)')),
                ('ontologyterm_unit', models.ForeignKey(blank=True, help_text='If the value has a unit, find an appropiate ontology term', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ontologyterm_unit', to='misa.OntologyTerm', verbose_name='Ontology Term (unit)')),
                ('ontologyterm_value', models.ForeignKey(blank=True, help_text="The value, e.g. if  wild type,If the ontology term is not available please  <a target='_blank' href='/misa/search_ontologyterm/'>add</a>.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ontologyterm_value', to='misa.OntologyTerm', verbose_name='Ontology Term (value)')),
            ],
        ),
        migrations.CreateModel(
            name='StudySample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_name', models.CharField(max_length=200)),
                ('organism', models.ForeignKey(blank=True, help_text="If factor not available then please   <a target='_blank' href='/misa/create_organism/'>add</a>.", null=True, on_delete=django.db.models.deletion.CASCADE, to='misa.Organism')),
                ('organism_part', models.ForeignKey(blank=True, help_text="If organism part not available then please   <a target='_blank' href='/misa/create_organismpart/'>add</a>.", null=True, on_delete=django.db.models.deletion.CASCADE, to='misa.OrganismPart')),
                ('samplecollectionprocess', models.ForeignKey(blank=True, help_text='The sample collection process used (will be added automatically)', null=True, on_delete=django.db.models.deletion.CASCADE, to='misa.SampleCollectionProcess')),
                ('sampletype', models.ForeignKey(help_text='This is an internal category that helps with some downstream processing essentialy ANIMAL covers all biological samples, COMPOUND is for chemical standards or non biological samples, and BLANK is for any samples that represent the blank (e.g. for  blank subtraction)', on_delete=django.db.models.deletion.CASCADE, to='misa.SampleType')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.Study')),
                ('studyfactor', models.ManyToManyField(blank=True, help_text="If factor not available then please   <a target='_blank' href='/misa/sfcreate/'>add</a>.", to='misa.StudyFactor')),
            ],
        ),
        migrations.AddField(
            model_name='speprotocol',
            name='spetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.SpeType'),
        ),
        migrations.AddField(
            model_name='speprocess',
            name='speprotocol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.SpeProtocol'),
        ),
        migrations.AddField(
            model_name='samplecollectionprocess',
            name='samplecollectionprocess',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.SampleCollectionProtocol'),
        ),
        migrations.AddField(
            model_name='metaboliteidentificationprocess',
            name='metaboliteidentificationprotocol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.MetaboliteIdentificationProtocol'),
        ),
        migrations.AddField(
            model_name='measurementtechnique',
            name='ontologyterm',
            field=models.ManyToManyField(to='misa.OntologyTerm'),
        ),
        migrations.AddField(
            model_name='measurementprotocol',
            name='measurementtechnique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.MeasurementTechnique'),
        ),
        migrations.AddField(
            model_name='measurementprocess',
            name='measurementprotocol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.MeasurementProtocol'),
        ),
        migrations.AddField(
            model_name='measurementprocess',
            name='polaritytype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.PolarityType'),
        ),
        migrations.AddField(
            model_name='extractiontype',
            name='ontologyterm',
            field=models.ManyToManyField(to='misa.OntologyTerm'),
        ),
        migrations.AddField(
            model_name='extractionprotocol',
            name='extractiontype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.ExtractionType'),
        ),
        migrations.AddField(
            model_name='extractionprocess',
            name='extractionprotocol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.ExtractionProtocol'),
        ),
        migrations.AddField(
            model_name='datatransformationprocess',
            name='datatransformationprotocol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.DataTransformationProtocol'),
        ),
        migrations.AddField(
            model_name='chromatographytype',
            name='ontologyterm',
            field=models.ManyToManyField(to='misa.OntologyTerm'),
        ),
        migrations.AddField(
            model_name='chromatographyprotocol',
            name='chromatographytype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.ChromatographyType'),
        ),
        migrations.AddField(
            model_name='chromatographyprocess',
            name='chromatographyprotocol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.ChromatographyProtocol'),
        ),
        migrations.AddField(
            model_name='assaydetail',
            name='chromatographyprocess',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.ChromatographyProcess'),
        ),
        migrations.AddField(
            model_name='assaydetail',
            name='datatransformationprocess',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='misa.DataTransformationProcess'),
        ),
        migrations.AddField(
            model_name='assaydetail',
            name='extractionprocess',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.ExtractionProcess'),
        ),
        migrations.AddField(
            model_name='assaydetail',
            name='measurementprocess',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.MeasurementProcess'),
        ),
        migrations.AddField(
            model_name='assaydetail',
            name='metaboliteidentifcationprocess',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='misa.MetaboliteIdentificationProcess'),
        ),
        migrations.AddField(
            model_name='assaydetail',
            name='speprocess',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.SpeProcess'),
        ),
        migrations.AddField(
            model_name='assaydetail',
            name='studysample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.StudySample'),
        ),
        migrations.AddField(
            model_name='assay',
            name='study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misa.Study'),
        ),
        migrations.AlterUniqueTogether(
            name='studysample',
            unique_together=set([('sample_name', 'study')]),
        ),
        migrations.AlterUniqueTogether(
            name='study',
            unique_together=set([('name', 'investigation')]),
        ),
        migrations.AlterUniqueTogether(
            name='assaydetail',
            unique_together=set([('code_field', 'assay')]),
        ),
        migrations.AlterUniqueTogether(
            name='assay',
            unique_together=set([('name', 'study')]),
        ),
    ]
