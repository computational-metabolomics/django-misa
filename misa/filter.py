import django_filters
from django_filters import rest_framework as filters
from gfiles.models import GenericFile
from misa.models import Investigation, Assay


class ISAFileFilter(filters.FilterSet):
    investigation =  django_filters.CharFilter('mfile__run__assayrun__assaydetail__assay__study__investigation__name',
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

            # 'galaxy_id': ['contains'],
            # 'accessible': ['isnull']
        }


class InvestigationFilter(filters.FilterSet):


    class Meta:
        model = Investigation

        fields = {
            'name': ['contains'],

            # 'galaxy_id': ['contains'],
            # 'accessible': ['isnull']
        }


class AssayFilter(filters.FilterSet):


    class Meta:
        model = Assay

        fields = {
            'name': ['contains'],

            # 'galaxy_id': ['contains'],
            # 'accessible': ['isnull']
        }