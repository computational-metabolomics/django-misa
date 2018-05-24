# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse_lazy
from django.db import models
# from django_mysql.models import Model
from metab.models import Run
from gfiles.models import GenericFile
from ckeditor.fields import RichTextField
import os, uuid
from datetime import datetime

def json_file_upload(process, filename):
    return os.path.join('uploads', 'misa', '{}_{}'.format(str(uuid.uuid4()), filename))


class OntologyTerm(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ontology_id = models.TextField(null=True, blank=True)
    iri = models.TextField(blank=True, null=True)
    obo_id = models.CharField(max_length=200, blank=True, null=True)
    ontology_name = models.CharField(max_length=200, blank=True, null=True)
    ontology_prefix = models.CharField(max_length=200, blank=True, null=True)
    short_form = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)



    def __str__(self):
        return '{} {}'.format(self.name, self.short_form)

ONTOLOGY_ADD_HELP = mark_safe("If the ontology term is not available, please "
                             " <a target='_blank' href='/misa/search_ontologyterm/'>add</a>.")

class Organism(models.Model):
    # need to update with proper ontologies
    ontologyterm = models.ForeignKey(OntologyTerm, on_delete=models.CASCADE,
                                     help_text=ONTOLOGY_ADD_HELP)
    name = models.TextField(blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def save(self, *args, **kwargs):
        # this allows it to be searchable with autocomplete functionaltiy
        self.name = self.ontologyterm.name
        super(Organism, self).save(*args, **kwargs)


class OrganismPart(models.Model):
    # need to update with proper ontologies
    ontologyterm = models.ForeignKey(OntologyTerm, on_delete=models.CASCADE,
                                     help_text=ONTOLOGY_ADD_HELP)

    name = models.TextField(blank=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def save(self, *args, **kwargs):
        # this allows it to be searchable with autocomplete functionaltiy
        self.name = self.ontologyterm.name
        super(OrganismPart, self).save(*args, **kwargs)




class Investigation(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    description = RichTextField(help_text='Investigation description')
    # json_file = models.FileField(upload_to=json_file_upload, blank=True, null=True, max_length=1000)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


    # def save(self, *args, **kwargs):
        # read in JSON and update other things e.g. Study, Study Samples, Assay and Assay Details
        # Create ISA files from json and save as zip in the investigation
        # super(Investigation, self).save(*args, **kwargs)
        #
        # misa = isajson.load(self.json_file)
        #
        # for s in isa.studies:
        #     study = Study(investigation=self)
        #     study.save()
        #     for samp in s.samples:
        #         print samp
        #         ss = StudySamples(study=study, sample_name=samp.name)
        #         ss.save()
        #     for a in s.assays:
        #         aa = Assay(study=study)
        #         aa.save()
                # then create the assay files. Example json are not suitable at the moment though. Have to get example
                # from David and also create a DMA based json to try out

# Any general files that need to be associated with the investigation
class MISAFile(GenericFile):
    investigation = models.ForeignKey(Investigation, on_delete=models.CASCADE)


class Study(models.Model):
    investigation = models.ForeignKey(Investigation, on_delete=models.CASCADE)
    description = RichTextField(help_text='Study description')
    dmastudy = models.BooleanField()
    name = models.CharField(max_length=100, blank=False, null=False, help_text='e.g. the study identifier')
    title = models.CharField(max_length=100, blank=True, null=True)
    grant_number = models.CharField(max_length=100, blank=True, null=True)
    funding_agency = models.CharField(max_length=100, blank=True, null=True)
    submission_date = models.DateTimeField(blank=True)
    public_release_date = models.DateTimeField(blank=True)

    study_design_descriptors = models.ManyToManyField(OntologyTerm,
                                                      help_text=mark_safe("Any ontological terms that can describe or 'tag' the study"
                                                               " <a target='_blank' href='/misa/search_ontologyterm/'>add</a>."))


    def __str__(self):              # __unicode__ on Python 2
        return 'INV: {} ||| STUDY: {}'.format(self.investigation, self.name)

    class Meta:
        unique_together = (("name", "investigation"),)


class StudyFactor(models.Model):
    ontologyterm_type = models.ForeignKey(OntologyTerm, on_delete=models.CASCADE,
                                          help_text=mark_safe("The type for the value e.g. gene knockout, concentration unit, etc"
                                                              " If the ontology term is not available please "
                                                              " <a target='_blank' href='/misa/search_ontologyterm/'>add</a>."),
                                                               verbose_name='Ontology Term (type)',
                                          null=True, blank=True, related_name='ontologyterm_type')
    ontologyterm_value = models.ForeignKey(OntologyTerm, on_delete=models.CASCADE,
                                                      help_text=mark_safe("The value, e.g. if  wild type, 5 Mol, etc "
                                                                "If the ontology term is not available please "
                                                               " <a target='_blank' href='/misa/search_ontologyterm/'>add</a>."),
                                                    verbose_name='Ontology Term (value)',
                                           null=True, blank=True, related_name='ontologyterm_value')

    value = models.CharField(max_length=100, blank=True, null=True,
                            help_text='If no appropiate ontological term for the value, then add free text here')

    def __str__(self):              # __unicode__ on Python 2
        if self.ontologyterm_value:
            return 'type: {}, value {},'.format(self.ontologyterm_type, self.ontologyterm_value)
        else:
            return 'type: {}, value {},'.format(self.ontologyterm_type, self.value)




class SampleType(models.Model):
    type = models.CharField(max_length=40, blank=True, null=True, unique=True)
    ontologyterm = models.ForeignKey(OntologyTerm, on_delete=models.CASCADE, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.type

class StudySample(models.Model):
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    sample_name = models.CharField(max_length=200)
    studyfactor = models.ManyToManyField(StudyFactor, blank=True,
                                         help_text= mark_safe("If factor not available then please  "
                                         " <a target='_blank' href='/misa/sfcreate/'>add</a>.")
                                         )
    organism = models.ForeignKey(Organism, blank=True, null=True,
                                 help_text= mark_safe("If factor not available then please  "
                                 " <a target='_blank' href='/misa/create_organism/'>add</a>.")
                                 )
    organism_part = models.ForeignKey(OrganismPart, blank=True, null=True,
                                      help_text=mark_safe("If organism part not available then please  "
                                                          " <a target='_blank' href='/misa/create_organismpart/'>add</a>.")
                                     )
    sampletype = models.ForeignKey(SampleType, on_delete=models.CASCADE, help_text='This is an internal category that'
                                                                                   ' helps with some downstream processing'
                                                                                   ' essentialy ANIMAL covers all biological samples,'
                                                                                   ' COMPOUND is for chemical standards or non biological samples,'
                                                                                   ' and BLANK is for any samples that represent the blank (e.g. for '
                                                                                   ' blank subtraction)')
    def __str__(self):              # __unicode__ on Python 2
        return self.sample_name

    class Meta:
        unique_together = (("sample_name", "study"),)


class Assay(models.Model):
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    description = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    # ontologyterm = models.ForeignKey(OntologyTerm, on_delete=models.CASCADE, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return '{} ||| ASSAY: {}'.format(self.study, self.name)

    class Meta:
        unique_together = (("name", "study"),)



class AssayRun(models.Model):
    assaydetail = models.ForeignKey('AssayDetail', on_delete=models.CASCADE)
    run = models.OneToOneField(Run, on_delete=models.CASCADE)
    technical_replicate = models.IntegerField(default=1, null=False)

    def __str__(self):              # __unicode__ on Python 2
        return '{}_RUN-{}'.format(self.assaydetail.code_field, self.run.id)


class ChromatographyType(models.Model):
    type = models.CharField(max_length=40, blank=True, null=True, unique=True)
    ontologyterm = models.ManyToManyField(OntologyTerm)

    def __str__(self):              # __unicode__ on Python 2
        return self.type

    def save(self, *args, **kwargs):
        # this allows it to be searchable with autocomplete functionaltiy
        self.type = self.ontologyterm.name
        super(ChromatographyType, self).save(*args, **kwargs)


class SpeType(models.Model):
    type = models.CharField(unique=True, max_length=30)
    ontologyterm = models.ForeignKey(OntologyTerm, on_delete=models.CASCADE, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.type


class ExtractionType(models.Model):
    type = models.CharField(unique=True, max_length=6)
    description = models.CharField(max_length=30, blank=True, null=True)
    ontologyterm = models.ManyToManyField(OntologyTerm)

    def __str__(self):              # __unicode__ on Python 2
        return self.type


class MeasurementTechnique(models.Model):
    type = models.CharField(max_length=40, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    ontologyterm = models.ManyToManyField(OntologyTerm)

    def __str__(self):              # __unicode__ on Python 2
        return self.type


class PolarityType(models.Model):
    type = models.CharField(max_length=30)
    ontologyterm = models.ForeignKey(OntologyTerm, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "polarity types"

    def __str__(self):              # __unicode__ on Python 2
        return self.type


def validate_workflow_code(value):

    code_l = value.split('_')

    if not len(code_l) == 7:
        raise ValidationError(
            _('%(value) is not in correct format, should have 7 components separated by "_", e.g.'
              'A_AP_WAX[4]_C30[96]_DI-MSn_NEG'),
            params={'value': value},
        )


class Protocol(models.Model):
    name = models.CharField(max_length=30)
    # protocoltype = models.ForeignKey(OntologyTerm, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    uri = models.CharField(max_length=200)
    version = models.CharField(max_length=30)
    code_field = models.CharField(max_length=20, null=False, unique=True)

    class Meta:
        abstract = True

    def __str__(self):              # __unicode__ on Python 2
        return self.code_field


class ExtractionProtocol(Protocol):
    extractiontype = models.ForeignKey(ExtractionType, on_delete=models.CASCADE)
    postextraction = models.CharField(max_length=300)
    derivitisation  = models.CharField(max_length=300)



class ExtractionProcess(models.Model):
    extractionprotocol = models.ForeignKey(ExtractionProtocol, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    details = models.CharField(max_length=300)


class ChromatographyProtocol(Protocol):
    chromatographytype = models.ForeignKey(ChromatographyType, on_delete=models.CASCADE)

    instrument_name = models.CharField(max_length=300)
    # instrument_name_ontology_term = models.ForeignKey(OntologyTerm, on_delete=models.CASCADE)
    # column_type_ontology_term = models.ForeignKey(OntologyTerm, on_delete=models.CASCADE)


class ChromatographyProcess(models.Model):
    chromatographyprotocol = models.ForeignKey(ChromatographyProtocol, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    details = models.CharField(max_length=300)
    chromatographyfrac = models.IntegerField()


class SpeProtocol(Protocol):
    spetype = models.ForeignKey(SpeType, on_delete=models.CASCADE)


class SpeProcess(models.Model):
    speprotocol = models.ForeignKey(SpeProtocol, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    details = models.CharField(max_length=300)
    spefrac = models.IntegerField()


class MeasurementProtocol(Protocol):
    measurementtechnique = models.ForeignKey(MeasurementTechnique, on_delete=models.CASCADE)


class MeasurementProcess(models.Model):
    measurementprotocol = models.ForeignKey(MeasurementProtocol, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    details = models.CharField(max_length=300)
    polaritytype = models.ForeignKey(PolarityType, on_delete=models.CASCADE)


class AssayDetail(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    code_field = models.CharField(db_column='code_', max_length=100,
                                  validators=[validate_workflow_code])

    studysample = models.ForeignKey(StudySample, on_delete=models.CASCADE)
    extractionprocess = models.ForeignKey(ExtractionProcess, on_delete=models.CASCADE)
    speprocess = models.ForeignKey(SpeProcess, on_delete=models.CASCADE)
    chromatographyprocess = models.ForeignKey(ChromatographyProcess, on_delete=models.CASCADE)
    measurementprocess = models.ForeignKey(MeasurementProcess, on_delete=models.CASCADE)


    class Meta:

        unique_together = (("code_field", "assay"),)

    def save(self, *args, **kwargs):
        sampletype = self.studysample.sample_name
        extraction = self.extractionprocess.extractionprotocol.extractiontype.type
        spe = self.speprocess.speprotocol.spetype.type
        spefrac = self.speprocess.spefrac
        lc = self.chromatographyprocess.chromatographyprotocol.chromatographytype.type
        lcfrac = self.chromatographyprocess.chromatographyfrac
        measurement =self.measurementprocess.measurementprotocol.measurementtechnique.type
        pol = self.measurementprocess.polaritytype.type

        self.code_field = '{}_{}_{}_{}_{}_{}_{}_{}'.format(
                            sampletype, extraction, spe, spefrac, lc, lcfrac, measurement, pol)
        super(AssayDetail, self).save(*args, **kwargs)


    def __str__(self):              # __unicode__ on Python 2
        return self.code_field