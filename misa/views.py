# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView, View
from django_tables2 import RequestConfig
from django.urls import reverse_lazy

from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from dal import autocomplete

from gfiles.models import GenericFile
from mbrowse.models import MFile

from misa.models import (
    Investigation,
    Assay,
    AssayDetail,
    Study,
    StudySample,
    StudyFactor,
    OntologyTerm,
    OrganismPart,
    Organism,
    ChromatographyProtocol,
    ChromatographyType,
    MeasurementProtocol,
    MeasurementTechnique,
    ExtractionProtocol,
    ExtractionType,
    SpeProtocol,
    SpeType
)

from misa.forms import (
    UploadAssayDataFilesForm,
    SearchOntologyTermForm,
    StudyFactorForm,
    StudyForm,
    OrganismPartForm,
    OrganismForm,
    StudySampleForm,
    ChromatographyProtocolForm,
    ChromatographyTypeForm,
    MeasurementProtocolForm,
    MeasurementTechniqueForm,
    ExtractionProtocolForm,
    ExtractionTypeForm,
    SpeProtocolForm,
    SpeTypeForm,
)

from misa.utils.isa_upload import upload_assay_data_files_zip
from misa.utils.create_isa_files import create_isa_files
from misa.utils.ontology_utils import search_ontology_term, search_ontology_term_shrt
from misa.tasks import upload_assay_data_files_dir_task
from misa.tables import AssayFileTable, AssayDetailTable, ISAFileSelectTable, InvestigationTable, AssayTable, OntologyTermTable
from misa.filter import ISAFileFilter, InvestigationFilter, AssayFilter
from django.shortcuts import redirect

def success(request):
    return render(request, 'misa/success.html')



############################################################################################
# Export json
############################################################################################
class ISAJsonExport(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        print self.kwargs
        inv = Investigation.objects.filter(pk=self.kwargs['pk'])
        print inv
        if inv:
            isa_out, json_out = create_isa_files(inv[0].id)

        else:
            json_out = {}

        return HttpResponse(json_out, content_type="application/json")









############################################################################################
# Adding ontology terms
############################################################################################
class OntologyTermCreateView(LoginRequiredMixin, CreateView):
    model = OntologyTerm
    success_url = '/misa/success'
    fields = '__all__'


class OntologyTermSearchView(LoginRequiredMixin, View):

    success_url = '/misa/success'
    redorect_to = '/misa/search_ontologyterm_result/'

    template_name = 'misa/searchontologyterm_form.html'
    def get(self, request, *args, **kwargs):

        form = SearchOntologyTermForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SearchOntologyTermForm(request.POST, request.FILES)

        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            res = search_ontology_term(search_term)
            request.session['res'] = res  # set in session
            return redirect(self.redorect_to)

            # return render(request, 'misa/ontology_search_results.html', {'table': ont_table})
        else:
            print form.errors

        return render(request, self.template_name, {'form': form})


class OntologyTermSearchResultView(LoginRequiredMixin, View):

    template_name = 'misa/ontology_search_results.html'
    def get(self, request, *args, **kwargs):
        res = request.session.get('res')
        ont_table = OntologyTermTable(res)
        RequestConfig(request).configure(ont_table)
        return render(request, self.template_name, {'table': ont_table})



class AddOntologyTermView(LoginRequiredMixin, CreateView):
    model = OntologyTerm
    success_url = '/misa/success'
    fields = '__all__'

    def get_initial(self):
        res = self.request.session.get('res')
        print res
        c = self.kwargs['c']
        for row in res:
            if row['c']==int(c):
                return row
        return {}





class OntologyTermAutocomplete(autocomplete.Select2QuerySetView):
    model_class = OntologyTerm

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return self.model_class.objects.none()

        qs = self.model_class.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


############################################################################################
# Organism Views
############################################################################################
class OrganismCreateView(LoginRequiredMixin, CreateView):
    model = Organism
    success_url = '/misa/success'
    form_class = OrganismForm


class OrganismPartCreateView(LoginRequiredMixin, CreateView):
    form_class = OrganismPartForm
    model = OrganismPart
    success_url = '/misa/success'


class OrganismAutocomplete(OntologyTermAutocomplete):
    model_class = Organism

class OrganismPartAutocomplete(OntologyTermAutocomplete):
    model_class = OrganismPart


############################################################################################
# Protocol views
###########################################################################################
class ChromatographyProtocolCreateView(LoginRequiredMixin, CreateView):
    model = ChromatographyProtocol
    form_class = ChromatographyProtocolForm
    success_url = '/misa/success'


class ChromatographyTypeCreateView(LoginRequiredMixin, CreateView):
    model = ChromatographyType
    form_class = ChromatographyTypeForm
    success_url = '/misa/success'


class ChromatographyTypeAutocomplete(OntologyTermAutocomplete):
    model_class = ChromatographyType


class MeasurementProtocolCreateView(LoginRequiredMixin, CreateView):
    model = MeasurementProtocol
    form_class = MeasurementProtocolForm
    success_url = '/misa/success'


class MeasurementTechniqueCreateView(LoginRequiredMixin, CreateView):
    model = MeasurementTechnique
    form_class = MeasurementTechniqueForm
    success_url = '/misa/success'


class MeasurementTechniqueAutocomplete(OntologyTermAutocomplete):
    model_class = MeasurementTechnique


class ExtractionProtocolCreateView(LoginRequiredMixin, CreateView):
    model = ExtractionProtocol
    form_class = ExtractionProtocolForm
    success_url = '/misa/success'


class ExtractionTypeCreateView(LoginRequiredMixin, CreateView):
    model = ExtractionType
    form_class = ExtractionTypeForm
    success_url = '/misa/success'


class ExtractionTypeAutocomplete(OntologyTermAutocomplete):
    model_class = ExtractionType


class SpeProtocolCreateView(LoginRequiredMixin, CreateView):
    model = SpeProtocol
    form_class = SpeProtocolForm
    success_url = '/misa/success'


class SpeTypeCreateView(LoginRequiredMixin, CreateView):
    model = SpeType
    form_class = SpeTypeForm
    success_url = '/misa/success'


class SpeTypeAutocomplete(OntologyTermAutocomplete):
    model_class = SpeType





############################################################################################
# Investigation views
############################################################################################
class InvestigationCreateView(LoginRequiredMixin, CreateView):
    model = Investigation
    success_msg = "Investigation created"
    success_url = '/misa/success'
    fields = '__all__'


class InvestigationUpdateView(LoginRequiredMixin, UpdateView):
    model = Investigation
    success_msg = "Investigation updated"
    success_url = '/misa/success'
    fields = '__all__'


class InvestigationDetailView(LoginRequiredMixin, DetailView):
    model = Investigation
    fields = '__all__'


class InvestigationDetailTablesView(LoginRequiredMixin, View):
    '''
    Run a registered workflow
    '''

    template_name = 'misa/investigation_detail_tables.html'
    table_class = AssayTable
    filter_class = AssayFilter


    def get_queryset(self):
        return Investigation.objects.get(pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):

        l, investigation = self.page_setup(request)

        return render(request, self.template_name, {'list': l, 'investigation': investigation})

    def page_setup(self, request):
        # Need to setup a config for the tables (only 1 required per template page)
        rc = RequestConfig(request, paginate={'per_page': 20})

        investigation = self.get_queryset()

        tables = []
        filters = []
        studies = []
        c = 0
        # loop through all the data_inputs from the associated workflow
        for s in investigation.study_set.all():
            assays = s.assay_set.all()

            # Create an invidivual filter for each table
            f = self.filter_class(request.GET, queryset=assays, prefix=c)

            # Create a checkbox column for each table, so that the javascript can see which checkbox has been
            # selected
            # create a new table with the custom column
            table = self.table_class(f.qs, prefix=c, attrs={'name': c, 'id': c, 'class': 'paleblue'})

            # load the table into the requestconfig
            rc.configure(table)

            # add the tables and filters to the list used in the template
            tables.append(table)
            filters.append(f)
            studies.append(s)
            c+=1

        # create a list of all the information. Using a simple list format as it is just easy to use in the template
        l = zip(studies, tables, filters)
        return l, investigation



class InvestigationListViewOLD(LoginRequiredMixin, ListView):
    model = Investigation
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(InvestigationListViewOLD, self).get_context_data(**kwargs)
        context['now'] = 1
        # Investigation.objects.filter(self.kwargs['company']).order_by('-pk')
        return context

class InvestigationListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    # table_class = ISAFileSelectTable
    # model = GenericFile
    # template_name = 'misa/isa_file_select.html'
    # filterset_class =  ISAFileFilter

    table_class = InvestigationTable
    model = Investigation
    template_name = 'misa/investigation_list.html'
    filterset_class = InvestigationFilter

    # def post(self, request, *args, **kwargs):
        # workflow_sync(request.user)
        # redirects to show the current available workflows
        # return redirect('workflow_summary')


############################################################################################
# Study views
############################################################################################
class StudyCreateView(LoginRequiredMixin, CreateView):
    model = Study
    success_url = '/misa/success'
    form_class = StudyForm


class StudyUpdateView(LoginRequiredMixin, UpdateView):
    model = Study
    success_url = '/misa/success'
    fields = '__all__'


class StudyListView(LoginRequiredMixin, ListView):
    model = Study
    fields = '__all__'


############################################################################################
# Assay views
############################################################################################
class AssayCreateView(LoginRequiredMixin, CreateView):
    model = Assay
    success_url = '/misa/success'
    fields = '__all__'


class AssayUpdateView(LoginRequiredMixin, UpdateView):
    model = Assay
    success_url = '/misa/success'
    fields = '__all__'

class AssayListView(LoginRequiredMixin, ListView):
    model = Assay
    fields = '__all__'



class UploadAssayDataFilesView(LoginRequiredMixin, View):

    success_msg = ""
    success_url = '/dma/success'
    # initial = {'key': 'value'}
    template_name = 'misa/upload_assay_data_files.html'

    def get(self, request, *args, **kwargs):
        form = UploadAssayDataFilesForm(user=self.request.user, assayid=self.kwargs['assayid'])

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UploadAssayDataFilesForm(request.user, request.POST, request.FILES, assayid=self.kwargs['assayid'])

        if form.is_valid():

            data_zipfile = form.cleaned_data['data_zipfile']
            data_mappingfile = form.cleaned_data['data_mappingfile']
            assayid = kwargs['assayid']
            create_assay_details = form.cleaned_data['create_assay_details']


            if data_zipfile:
                upload_assay_data_files_zip(assayid, data_zipfile, data_mappingfile, request.user, create_assay_details)
                return render(request, 'dma/success.html')
            else:
                save_as_link = form.cleaned_data['save_as_link']
                # recursive = form.cleaned_data['recursive']
                # dir_pths = get_pths_from_field(form.dir_fields, form.cleaned_data, request.user.username)

                # rstring = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
                # unique_folder = os.path.join(settings.MEDIA_ROOT, 'mapping', rstring)
                # os.makedirs(unique_folder)
                # data_mappingfile_pth = os.path.join(unique_folder, data_mappingfile.name)
                # with default_storage.open(data_mappingfile_pth, 'wb+') as destination:
                #     for chunk in data_mappingfile.chunks():
                #         print chunk
                #         destination.write(chunk)

                # mapping_l = list(csv.DictReader(data_mappingfile))

                result = upload_assay_data_files_dir_task.delay(form.filelist, request.user.username,
                                                                form.mapping_l, assayid, save_as_link,
                                                                create_assay_details)
                request.session['result'] = result.id
                return render(request, 'gfiles/status.html', {'s': 0, 'progress': 0})


        return render(request, self.template_name, {'form': form})


class AssayDeleteView(DeleteView):
    model = Assay
    success_url = reverse_lazy('misa/ilist')



############################################################################################
# Study sample views
############################################################################################
class StudySampleCreateView(LoginRequiredMixin, CreateView):
    form_class = StudySampleForm
    model = StudySample
    success_url = '/misa/success'



class StudySampleUpdateView(LoginRequiredMixin, UpdateView):
    model = StudySample
    success_url = '/misa/success'
    fields = '__all__'

class StudySampleListView(LoginRequiredMixin, ListView):
    model = StudySample
    fields = '__all__'


############################################################################################
# Study factor views
############################################################################################
class StudyFactorCreateView(LoginRequiredMixin, CreateView):
    model = StudyFactor
    success_url = '/misa/success'

    form_class = StudyFactorForm

class StudyFactorUpdateView(LoginRequiredMixin, UpdateView):
    model = StudyFactor
    success_url = '/misa/success'
    fields = '__all__'

class StudyFactorListView(LoginRequiredMixin, ListView):
    model = StudyFactor
    fields = '__all__'




############################################################################################
# Assay file views
###########################################################################################
class ISAFileSummaryView(LoginRequiredMixin, SingleTableMixin, FilterView):
    '''
    View and initiate a run for all registered workflows.

    Workflows can also be synced here as well
    '''
    table_class = ISAFileSelectTable
    model = GenericFile
    template_name = 'misa/isa_file_select.html'
    filterset_class =  ISAFileFilter

    # def post(self, request, *args, **kwargs):
    #     workflow_sync(request.user)
    #     # redirects to show the current available workflows
    #     return redirect('workflow_summary')




class AssayFileSummaryView(LoginRequiredMixin, View):

    # initial = {'key': 'value'}
    template_name = 'misa/assay_files.html'

    def get(self, request, *args, **kwargs):
        mfiles = MFile.objects.filter(run__assayrun__assaydetail__assay_id=kwargs['assayid'])
        table = AssayFileTable(mfiles)
        RequestConfig(request).configure(table)

        i = Investigation.objects.get(study__assay__id=kwargs['assayid'])

        return render(request, self.template_name,  {'table': table, 'investigation_id':i.id})

    # def post(self, request, *args, **kwargs):
    #     form = UploadAssayDataFilesForm(request.POST, request.FILES, assayid=self.kwargs['assayid'])
    #
    #     if form.is_valid():
    #
    #         data_zipfile = form.cleaned_data['data_zipfile']
    #         data_mappingfile = form.cleaned_data['data_mappingfile']
    #         assayid = kwargs['assayid']
    #         upload_assay_data_files(assayid, data_zipfile, data_mappingfile)
    #
    #         # result = update_workflows_task.delay(self.kwargs['dmaid'])
    #         # request.session['result'] = result.id
    #         return render(request, 'dma/submitted.html')
    #
    #     return render(request, self.template_name, {'form': form})


class AssayDetailSummaryView(LoginRequiredMixin, View):

    # initial = {'key': 'value'}
    template_name = 'misa/assay_details.html'

    def get(self, request, *args, **kwargs):
        mfiles = AssayDetail.objects.filter(assay_id=kwargs['assayid'])
        table = AssayDetailTable(mfiles)
        RequestConfig(request).configure(table)
        i = Investigation.objects.get(study__assay__id=kwargs['assayid'])

        return render(request, self.template_name,  {'table': table, 'investigation_id':i.id})




