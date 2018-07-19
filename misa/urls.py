from django.conf.urls import url
from misa import views

from misa.models import OntologyTerm
from dal import autocomplete

urlpatterns = [
    url(r'^create_ontologyterm/$', views.OntologyTermCreateView.as_view(), name='create_ontologyterm'),
    url(r'^search_ontologyterm/$', views.OntologyTermSearchView.as_view(), name='search_ontologyterm'),
    url(r'^search_ontologyterm_result/$', views.OntologyTermSearchResultView.as_view(), name='search_ontologyterm_result'),
    url(r'^add_ontologyterm/(?P<c>\d+)/$', views.AddOntologyTermView.as_view(), name='add_ontologyterm'),
    url(r'^ontologyterm-autocomplete/$', views.OntologyTermAutocomplete.as_view(), name='ontologyterm-autocomplete'),
    url(r'^ontologyterm-autocompleteTEST/$', autocomplete.Select2QuerySetView.as_view(model=OntologyTerm),name='select2_fk',),

    url(r'^create_organism/$', views.OrganismCreateView.as_view(), name='create_organism'),
    url(r'^create_organismpart/$', views.OrganismPartCreateView.as_view(), name='create_organismpart'),
    url(r'^organismpart-autocomplete/$', views.OrganismPartAutocomplete.as_view(), name='organismpart-autocomplete'),
    url(r'^organism-autocomplete/$', views.OrganismAutocomplete.as_view(), name='organism-autocomplete'),

    url(r'^cp_create/$', views.ChromatographyProtocolCreateView.as_view(), name='cp_create'),
    url(r'^cpt_create/$', views.ChromatographyTypeCreateView.as_view(), name='cpt_create'),
    url(r'^chromatographytype-autocomplete/$', views.ChromatographyTypeAutocomplete.as_view(), name='chromatographytype-autocomplete'),

    url(r'^mp_create/$', views.MeasurementProtocolCreateView.as_view(), name='mp_create'),
    url(r'^mpt_create/$', views.MeasurementTechniqueCreateView.as_view(), name='mpt_create'),
    url(r'^measurementtechnique-autocomplete/$', views.MeasurementTechniqueAutocomplete.as_view(), name='measurementtechnique-autocomplete'),

    url(r'^ep_create/$', views.ExtractionProtocolCreateView.as_view(), name='ep_create'),
    url(r'^ept_create/$', views.ExtractionTypeCreateView.as_view(), name='ept_create'),
    url(r'^extractiontype-autocomplete/$', views.ExtractionTypeAutocomplete.as_view(), name='extractiontype-autocomplete'),

    url(r'^sp_create/$', views.SpeProtocolCreateView.as_view(), name='sp_create'),
    url(r'^spt_create/$', views.SpeTypeCreateView.as_view(), name='spt_create'),
    url(r'^spetype-autocomplete/$', views.SpeTypeAutocomplete.as_view(), name='spetype-autocomplete'),

    url(r'^export_isa_json/(?P<pk>\d+)/$', views.ISAJsonExport.as_view(), name='export_isa_json'),

    url(r'^icreate/$', views.InvestigationCreateView.as_view(), name='icreate'),
    url(r'^iupdate/(?P<pk>\d+)/$', views.InvestigationUpdateView.as_view(), name='iupdate'),
    url(r'^idetail/(?P<pk>\d+)/$', views.InvestigationDetailView.as_view(), name='idetail'),
    url(r'^idetail_tables/(?P<pk>\d+)/$', views.InvestigationDetailTablesView.as_view(), name='idetail_tables'),
    url(r'^ilist/$', views.InvestigationListView.as_view(), name='ilist'),

    url(r'^screate/$', views.StudyCreateView.as_view(), name='screate'),
    url(r'^supdate/(?P<pk>\d+)/$', views.StudyUpdateView.as_view(), name='supdate'),
    url(r'^slist/$', views.StudyListView.as_view(), name='slist'),

    url(r'^acreate/$', views.AssayCreateView.as_view(), name='acreate'),
    url(r'^aupdate/(?P<pk>\d+)/$', views.AssayUpdateView.as_view(), name='aupdate'),
    url(r'^alist/$', views.AssayListView.as_view(), name='alist'),

    url(r'^smcreate/$', views.StudySampleCreateView.as_view(), name='smcreate'),
    url(r'^smupdate/(?P<pk>\d+)/$', views.StudySampleUpdateView.as_view(), name='smupdate'),
    url(r'^smlist/$', views.StudySampleListView.as_view(), name='smlist'),

    url(r'^sfcreate/$', views.StudyFactorCreateView.as_view(), name='sfcreate'),
    url(r'^sfupdate/(?P<pk>\d+)/$', views.StudyFactorUpdateView.as_view(), name='sfupdate'),
    url(r'^sflist/$', views.StudyFactorListView.as_view(), name='sflist'),

    url(r'^upload_assay_data_files/(?P<assayid>\d+)$', views.UploadAssayDataFilesView.as_view(), name='upload_assay_data_files'),

    url(r'^view_isa_data_files/$', views.ISAFileSummaryView.as_view(), name='view_isa_data_files'),


    url(r'^assayfile_summary/(?P<assayid>\d+)$', views.AssayFileSummaryView.as_view(), name='assayfile_summary'),
    url(r'^assaydetail_summary/(?P<assayid>\d+)$', views.AssayDetailSummaryView.as_view(), name='assaydetail_summary'),


    url(r'^success/$', views.success, name='success'),
    url(r'^adelete/(?P<pk>[\w]+)/$', views.AssayDeleteView.as_view(), name='adelete')

]