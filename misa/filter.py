# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from dal import autocomplete
import django_filters
from django_filters import rest_framework as filters
from gfiles.models import GenericFile
from misa.models import (
    ExtractionProtocol,
    ExtractionType,
    SpeProtocol,
    SpeType,
    ChromatographyProtocol,
    ChromatographyType,
    MeasurementTechnique,
    MeasurementProtocol,
    SampleCollectionProtocol,
    DataTransformationProtocol,
    Investigation,
    Assay,
    OntologyTerm,
    StudySample,
    StudyFactor,
    Organism,
    OrganismPart

)


class ISAFileFilter(filters.FilterSet):
    investigation = django_filters.CharFilter('mfile__run__assayrun__assaydetail__assay__study__investigation__name',
                                  lookup_expr='contains', label="Investigation contains")

    study = django_filters.CharFilter('mfile__run__assayrun__assaydetail__assay__study__name',
                                              lookup_expr='contains', label="Study contains")

    assay = django_filters.CharFilter('mfile__run__assayrun__assaydetail__assay__name',
                                              lookup_expr='contains', label="Assay contains")

    sample_name = django_filters.CharFilter('mfile__run__assayrun__assaydetail__studysample__sample_name',
                                      lookup_expr='contains', label="Sample name contains")

    technical_replicate = django_filters.CharFilter('mfile__run__assayrun__technical_replicate',
                                            lookup_expr='contains', label="technical_replicate contains")

    spe_type = django_filters.CharFilter('mfile__run__assayrun__assaydetail__speprocess__speprotocol__spetype__type',
                                                    lookup_expr='contains', label="SPE type contains")

    spe_frac = django_filters.CharFilter('mfile__run__assayrun__assaydetail__speprocess__spefrac',
                                         lookup_expr='contains', label="SPE frac contains")

    chromatography = django_filters.CharFilter(
        'mfile__run__assayrun__assaydetail__chromatographyprocess__chromatographyprotocol__chromatographytype__type',
        lookup_expr='contains', label="Chromatography contains")

    chromatographyfrac = django_filters.CharFilter(
        'mfile__run__assayrun__assaydetail__chromatographyprocess__chromatographyfrac',
        lookup_expr='contains', label="Chromatography frac contains")

    measurement = django_filters.CharFilter(
        'mfile__run__assayrun__assaydetail__measurementprocess__measurementprotocol__measurementtechnique__type',
        lookup_expr='contains', label="Measurement contains")

    polarity = django_filters.CharFilter(
        'mfile__run__assayrun__assaydetail__measurementprocess__polaritytype__type',
        lookup_expr='contains', label="Polarity contains")

    filesuffix = django_filters.CharFilter(
        'mfile__mfilesuffix__suffix',
        lookup_expr='contains', label="FileSuffix contains")


    #
    #
    #
    #
    #
    # original_filename = tables.Column(accessor='original_filename',
    #                                   verbose_name='Original file name')
    #


    class Meta:
        model = GenericFile

        fields = {
            'original_filename': ['contains'],
        }


class InvestigationFilter(filters.FilterSet):

    class Meta:
        model = Investigation

        fields = {
            'name': ['contains'],

        }


class AssayFilter(filters.FilterSet):

    class Meta:
        model = Assay

        fields = {
            'name': ['contains'],
        }


class ExtractionProtocolFilter(filters.FilterSet):

    class Meta:
        model = ExtractionProtocol

        fields = {
            'name': ['contains']
        }


class ExtractionTypeFilter(filters.FilterSet):

    class Meta:
        model = ExtractionType

        fields = {
            'type': ['contains']
        }


class SpeProtocolFilter(filters.FilterSet):

    class Meta:
        model = SpeProtocol

        fields = {
            'name': ['contains']
        }


class SpeTypeFilter(filters.FilterSet):

    class Meta:
        model = SpeType

        fields = {
            'type': ['contains']
        }


class ChromatographyProtocolFilter(filters.FilterSet):

    class Meta:
        model = ChromatographyProtocol

        fields = {
            'name': ['contains']
        }

class ChromatographyTypeFilter(filters.FilterSet):

    class Meta:
        model = ChromatographyType

        fields = {
            'type': ['contains']
        }


class MeasurementProtocolFilter(filters.FilterSet):

    class Meta:
        model = MeasurementProtocol

        fields = {
            'name': ['contains']
        }

class MeasurementTechniqueFilter(filters.FilterSet):

    class Meta:
        model = MeasurementTechnique

        fields = {
            'type': ['contains']
        }


class SampleCollectionProtocolFilter(filters.FilterSet):

    class Meta:
        model = SampleCollectionProtocol

        fields = {
            'name': ['contains']
        }


class DataTransformationProtocolFilter(filters.FilterSet):

    class Meta:
        model = DataTransformationProtocol

        fields = {
            'name': ['contains']
        }


class OntologyTermFilter(filters.FilterSet):

    class Meta:
        model = OntologyTerm

        fields = {
            'name': ['contains'],
            'iri': ['contains'],
            'ontology_id': ['contains'],
            'obo_id': ['contains'],
            'ontology_name': ['contains'],
            'ontology_prefix': ['contains'],
            'type': ['contains'],
            'short_form': ['contains']
        }


class StudySampleFilter(filters.FilterSet):

    class Meta:
        model = StudySample

        fields = {
            'sample_name': ['contains'],
        }


class StudyFactorFilter(filters.FilterSet):
    type = django_filters.CharFilter('ontologyterm_type__name', lookup_expr='contains',
                                   label="Study Factor Type")

    value_ont = django_filters.CharFilter('ontologyterm_value__name', lookup_expr='contains',
                                   label="Study Factor Value")

    value = django_filters.CharFilter('value', lookup_expr='contains',
                                   label="Study Factor Value (non ontological term)")

    unit = django_filters.CharFilter('value', lookup_expr='contains',
                                   label="Study Factor Unit")


    class Meta:
        model = StudyFactor
        # fields = '__all__'
        # fields = ('type', 'value_ont', 'value', 'unit')
        fields = ('type', 'value_ont', 'value', 'unit')


class OrganismFilter(filters.FilterSet):
    class Meta:
        model = Organism
        fields = ('name',)


class OrganismPartFilter(filters.FilterSet):
    class Meta:
        model = OrganismPart
        fields = ('name',)
