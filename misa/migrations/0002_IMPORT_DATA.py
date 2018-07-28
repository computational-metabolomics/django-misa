# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

def save_model_list_migration(l,db_alias):
    [i.save(using=db_alias) for i in l]

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Organism = apps.get_model("misa", "Organism")
    SampleType = apps.get_model("misa", "SampleType")
    MeasurementTechnique = apps.get_model("misa", "MeasurementTechnique")
    PolarityType = apps.get_model("misa", "PolarityType")
    ExtractionType = apps.get_model("misa", "ExtractionType")
    SpeType = apps.get_model("misa", "SpeType")
    ChromatographyType = apps.get_model("misa", "ChromatographyType")

    ExtractionProtocol = apps.get_model("misa", "ExtractionProtocol")
    SpeProtocol = apps.get_model("misa", "SpeProtocol")
    ChromatographyProtocol = apps.get_model("misa", "ChromatographyProtocol")
    MeasurementProtocol = apps.get_model("misa", "MeasurementProtocol")

    sample_class_input = ['ANIMAL', 'BLANK', 'COMPOUND']
    m_input = ['DI-MS', 'DI-MSn', 'LC-MS', 'LC-MSMS']
    p_input = ['POSITIVE', 'NEGATIVE', 'NA']
    extraction_input = ['AP', 'P']
    spe_input = ['WAX', 'WCX', 'C18', 'AMP', 'NA']
    lc_input = ['PHE', 'C30', 'C18', 'AMD', 'NA']

    db_alias = schema_editor.connection.alias

    o = Organism(name='Daphnia pulex')
    o.save(using=db_alias)

    o = Organism(name='Daphnia magna')
    o.save(using=db_alias)

    sampletypes = [SampleType.objects.create(type=i) for i in sample_class_input]
    measurement_techniques = [MeasurementTechnique.objects.create(type=i) for i in m_input]
    polaritietypes = [PolarityType.objects.create(type=i) for i in p_input]
    extractiontypes = [ExtractionType.objects.create(type=e) for e in extraction_input]
    spetypes = [SpeType.objects.create(type=e) for e in spe_input]
    chromtypes = [ChromatographyType.objects.create(type=e) for e in lc_input]

    save_model_list_migration(extractiontypes, db_alias)
    save_model_list_migration(spetypes, db_alias)
    save_model_list_migration(chromtypes, db_alias)
    save_model_list_migration(measurement_techniques, db_alias)
    save_model_list_migration(sampletypes, db_alias)
    save_model_list_migration(polaritietypes, db_alias)

    # mfs = MFileSuffix(suffix='.mzml')
    # mfs.save()
    # mfr = MFileSuffix(suffix='.raw')
    # mfr.save()

    # Create extraction protocol
    # extraction_protocols = [ExtractionProtocol(extractiontype=e, code_field='{}-1'.format(e)) in extractiontypes]
    for e in extractiontypes:
        p = ExtractionProtocol(extractiontype=e, code_field='{}'.format(e.type))
        p.save(using=db_alias)

    # Create SPE protocol
    for e in spetypes:
        p = SpeProtocol(spetype=e, code_field='{}'.format(e.type))
        p.save(using=db_alias)

    # Create SPE protocol
    for e in chromtypes:
        p = ChromatographyProtocol(chromatographytype=e, code_field='{}'.format(e.type))
        p.save(using=db_alias)

    for e in measurement_techniques:
        p = MeasurementProtocol(measurementtechnique=e, code_field='{}'.format(e.type))
        p.save(using=db_alias)


def reverse_func(apps, schema_editor):
    # forwards_func() creates two instances
    # so reverse_func() should delete them.
    SampleType = apps.get_model("misa", "SampleType")
    MeasurementTechnique = apps.get_model("misa", "MeasurementTechnique")
    PolarityType = apps.get_model("misa", "PolarityType")
    ExtractionType = apps.get_model("misa", "ExtractionType")
    SpeType = apps.get_model("misa", "SpeType")
    ChromatographyType = apps.get_model("misa", "ChromatographyType")

    # ExtractionProtocol = apps.get_model("misa", "ExtractionProtocol")
    # SpeProtocol = apps.get_model("misa", "SpeProtocol")
    # ChromatographyProtocol = apps.get_model("misa", "ChromatographyProtocol")
    # MeasurementProtocol = apps.get_model("misa", "MeasurementProtocol")
    #

    db_alias = schema_editor.connection.alias

    sample_class_input = ['ANIMAL', 'BLANK', 'COMPOUND']
    m_input = ['DI-MS', 'DI-MSn', 'LC-MS', 'LC-MSMS']
    p_input = ['POSITIVE', 'NEGATIVE', 'NA']
    extraction_input = ['AP', 'P', 'COMBINED']
    spe_input = ['WAX', 'WCX', 'C18']
    lc_input = ['PHE', 'C30', 'C18']



    SampleType.objects.using(db_alias).filter(type__in=sample_class_input).delete()
    MeasurementTechnique.objects.using(db_alias).filter(type__in=m_input).delete()
    PolarityType.objects.using(db_alias).filter(type__in=p_input).delete()
    ExtractionType.objects.using(db_alias).filter(type__in=extraction_input).delete()
    SpeType.objects.using(db_alias).filter(type__in=spe_input).delete()
    ChromatographyType.objects.using(db_alias).filter(type__in=lc_input).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('misa', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]

