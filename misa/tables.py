import django_tables2 as tables
from mbrowse.models import MFile
from misa.models import AssayDetail, Investigation, Assay, OntologyTerm
from django_tables2_column_shifter.tables import ColumnShiftTable
from gfiles.models import GenericFile
from django_tables2.utils import A

class AssayFileTable(ColumnShiftTable):
    sample_name = tables.Column(accessor='run.assayrun.assaydetail.studysample.sample_name',
                                verbose_name='Sample name')

    technical_replicate = tables.Column(accessor='run.assayrun.technical_replicate',
                        verbose_name='tech replicate')

    spetype = tables.Column(accessor='run.assayrun.assaydetail.speprocess.speprotocol.spetype.type',
                             verbose_name='SPE type')

    spefrac = tables.Column(accessor='run.assayrun.assaydetail.speprocess.spefrac',
                        verbose_name='SPE frac')

    chromatography = tables.Column(accessor='run.assayrun.assaydetail.chromatographyprocess.chromatographyprotocol.chromatographytype.type',
                             verbose_name='Chromatography')

    chromatographyfrac = tables.Column(accessor='run.assayrun.assaydetail.chromatographyprocess.chromatographyfrac',
                                   verbose_name='Chromatography frac')

    measurement = tables.Column(accessor='run.assayrun.assaydetail.measurementprocess.measurementprotocol.measurementtechnique.type',
                                        verbose_name='Measurement')

    polarity = tables.Column(accessor='run.assayrun.assaydetail.measurementprocess.polaritytype.type',
                                verbose_name='Polarity')

    code_field = tables.Column(accessor='run.assayrun.assaydetail.code_field',
                               verbose_name='Code field')

    class Meta:
        model = MFile
        attrs = {'class': 'paleblue'}
        template = 'django_tables2/bootstrap.html'
        fields = ('id','original_filename', 'data_file')


class AssayDetailTable(ColumnShiftTable):

    sample_name = tables.Column(accessor='studysample.sample_name',
                                verbose_name='Sample name')

    spetype = tables.Column(accessor='speprocess.speprotocol.spetype.type',
                             verbose_name='SPE type')

    spefrac = tables.Column(accessor='speprocess.spefrac',
                        verbose_name='SPE frac')

    chromatography = tables.Column(accessor='chromatographyprocess.chromatographyprotocol.chromatographytype.type',
                             verbose_name='Chromatography')

    chromatographyfrac = tables.Column(accessor='chromatographyprocess.chromatographyfrac',
                                   verbose_name='Chromatography frac')

    measurement = tables.Column(accessor='measurementprocess.measurementprotocol.measurementtechnique.type',
                                        verbose_name='Measurement')

    polarity = tables.Column(accessor='measurementprocess.polaritytype.type',
                                verbose_name='Polarity')

    code_field = tables.Column(accessor='code_field',
                               verbose_name='Code field')

    class Meta:
        model = AssayDetail
        attrs = {'class': 'paleblue'}
        template = 'django_tables2/bootstrap.html'
        fields = ('id',)




class ISAFileSelectTable(ColumnShiftTable):

    user = tables.Column(accessor='user',
                         verbose_name='user')

    file = tables.Column(accessor='data_file',
                         verbose_name='Full path')

    non_mfile_investigation = tables.Column(accessor='misafile.investigation',
                         verbose_name='Investigation (non-mfile)')

    original_filename = tables.Column(accessor='original_filename',
                                      verbose_name='File name')

    filesuffix = tables.Column(accessor='mfile.mfilesuffix.suffix',
                               verbose_name='File suffix')

    investigation = tables.Column(accessor='mfile.run.assayrun.assaydetail.assay.study.investigation.name',
                            verbose_name='Investigation')

    study = tables.Column(accessor='mfile.run.assayrun.assaydetail.assay.study.name',
                                  verbose_name='Study')

    assay = tables.Column(accessor='mfile.run.assayrun.assaydetail.assay.name',
                          verbose_name='Assay')

    sample_name = tables.Column(accessor='mfile.run.assayrun.assaydetail.studysample.sample_name',
                                verbose_name='Sample name')


    technical_replicate = tables.Column(accessor='mfile.run.assayrun.technical_replicate',
                                        verbose_name='tech replicate')

    spetype = tables.Column(accessor='mfile.run.assayrun.assaydetail.speprocess.speprotocol.spetype.type',
                            verbose_name='SPE type')

    spefrac = tables.Column(accessor='mfile.run.assayrun.assaydetail.speprocess.spefrac',
                            verbose_name='SPE frac')

    chromatography = tables.Column(
        accessor='mfile.run.assayrun.assaydetail.chromatographyprocess.chromatographyprotocol.chromatographytype.type',
        verbose_name='Chromatography')

    chromatographyfrac = tables.Column(accessor='mfile.run.assayrun.assaydetail.chromatographyprocess.chromatographyfrac',
                                       verbose_name='Chromatography frac')

    measurement = tables.Column(
        accessor='mfile.run.assayrun.assaydetail.measurementprocess.measurementprotocol.measurementtechnique.type',
        verbose_name='Measurement')

    polarity = tables.Column(accessor='mfile.run.assayrun.assaydetail.measurementprocess.polaritytype.type',
                             verbose_name='Polarity')

    code_field = tables.Column(accessor='mfile.run.assayrun.assaydetail.code_field',
                             verbose_name='Code field')


    def get_column_default_show(self):
        self.column_default_show = ['id', 'user', 'original_filename', 'sample_name', 'technical_replicate', 'study', 'assay']
        return super(ISAFileSelectTable, self).get_column_default_show()

    class Meta:
        model = GenericFile
        attrs = {'class': 'paleblue'}
        template = 'django_tables2/bootstrap.html'
        fields = ('id',)





class ISAFileSelectTableWithCheckBox(ISAFileSelectTable):

    check = tables.CheckBoxColumn(accessor="pk",
                                  attrs={
                                      "th__input": {"onclick": "toggle(this)"},
                                      "td__input": {"onclick": "addfile(this)"}},
                                  orderable=False)

    class Meta:
        model = GenericFile
        attrs = {'class': 'paleblue'}
        template = 'django_tables2/bootstrap.html'
        fields = ('id',)

    def get_column_default_show(self):
        self.column_default_show = ['id', 'user', 'original_filename', 'sample_name', 'technical_replicate',
                                    'investigation', 'study', 'assay', 'check']
        return super(ISAFileSelectTableWithCheckBox, self).get_column_default_show()




class InvestigationTable(ColumnShiftTable):
    details = tables.LinkColumn('idetail_tables', text='details', args=[A('id')])
    export = tables.LinkColumn('export_isa_json', text='export', verbose_name='Export ISA-JSON', args=[A('id')])

    class Meta:
        model = Investigation
        attrs = {'class': 'paleblue'}
        template = 'django_tables2/bootstrap.html'
        fields = ('id','name','description', 'details')


class AssayTable(tables.Table):
    upload = tables.LinkColumn('upload_assay_data_files',  text='upload', verbose_name='Upload Assay Data Files', args=[A('id')])
    details = tables.LinkColumn('assaydetail_summary', text='details',verbose_name='Assay details', args=[A('id')])
    files = tables.LinkColumn('assayfile_summary',  text='files', verbose_name='Assay files', args=[A('id')])
    delete = tables.LinkColumn('adelete', text='delete', verbose_name='Delete', args=[A('id')])



    class Meta:
        model = Assay
        attrs = {'class': 'paleblue'}
        template = 'django_tables2/bootstrap.html'
        fields = ('id', 'name',)


class OntologyTermTable(ColumnShiftTable):
    add = tables.LinkColumn('add_ontologyterm', text='add', verbose_name='Add Ontology Term',
                               args=[A('c')])

    c = tables.Column(verbose_name='Match count')

    class Meta:
        model = OntologyTerm
        attrs = {'class': 'paleblue'}
        template = 'django_tables2/bootstrap.html'

