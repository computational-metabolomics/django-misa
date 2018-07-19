# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from __future__ import unicode_literals

# from dma.utils import save_model_list



from misa.models import ChromatographyType, SpeType, ExtractionType, MeasurementTechnique, SampleType, PolarityType
from misa.models import ExtractionProtocol, SpeProtocol, ChromatographyProtocol, MeasurementProtocol
from misa.models import ExtractionProcess, SpeProcess, ChromatographyProcess, MeasurementProcess
from misa.models import Investigation, Study, StudySample, Assay
from misa.forms import AssayDetailForm

def save_model_list(l):
    [i.save() for i in l]

def protocol_setup(self):
    self.investigation = Investigation()
    self.investigation.save()
    self.study = Study(investigation=self.investigation, dmastudy=True)
    self.study.save()

    sampletypes = SampleType.objects.all()

    sample1 = StudySample(study=self.study, sample_name='ANIMAL', sampletype=sampletypes[0])
    sample1.save()

    sample2 = StudySample(study=self.study, sample_name='BLANK', sampletype=sampletypes[1])
    sample2.save()

    assay = Assay(study=self.study, description='P_WAX[1]_PHE[0]_LC-MS_LC-MSMS')
    assay.save()

    self.assay = assay


def upload_assay_data_form_setup(self):

    protocol_setup(self)

    codes_in = [{'sample': 'ANIMAL', 'extraction': 'P', 'spe': 'WAX', 'spefrac': 1, 'chromatography':'PHE', 'chromatographyfrac': 0, 'measurement': 'LC-MS', 'polarity': 'POSITIVE'},
                {'sample': 'ANIMAL', 'extraction': 'P', 'spe': 'WAX', 'spefrac': 1, 'chromatography':'PHE', 'chromatographyfrac': 0, 'measurement': 'LC-MS', 'polarity': 'NEGATIVE'},

                {'sample': 'BLANK', 'extraction': 'P', 'spe': 'WAX', 'spefrac': 1, 'chromatography':'PHE', 'chromatographyfrac': 0, 'measurement': 'LC-MS', 'polarity': 'POSITIVE'},
                {'sample': 'BLANK', 'extraction': 'P', 'spe': 'WAX', 'spefrac': 1, 'chromatography':'PHE', 'chromatographyfrac': 0, 'measurement': 'LC-MS', 'polarity': 'NEGATIVE'},

                {'sample': 'ANIMAL', 'extraction': 'P', 'spe': 'WAX', 'spefrac': 1, 'chromatography':'PHE', 'chromatographyfrac': 0, 'measurement': 'LC-MSMS', 'polarity': 'POSITIVE'},
                {'sample': 'ANIMAL', 'extraction': 'P', 'spe': 'WAX', 'spefrac': 1, 'chromatography':'PHE', 'chromatographyfrac': 0, 'measurement': 'LC-MSMS', 'polarity': 'NEGATIVE'}
                ]


    for c in codes_in:
        # Create extraction process
        ei = ExtractionProcess(extractionprotocol=ExtractionProtocol.objects.filter(code_field=c['extraction'])[0])
        ei.save()

        # Create SPE process
        spei = SpeProcess(spefrac=1, speprotocol=SpeProtocol.objects.filter(code_field=c['spe'])[0])
        spei.save()

        # Create chromtography process
        ci = ChromatographyProcess(chromatographyfrac=0, chromatographyprotocol=ChromatographyProtocol.objects.filter(code_field=c['chromatography'])[0])
        ci.save()

        # create measurement process
        mi = MeasurementProcess(measurementprotocol=MeasurementProtocol.objects.filter(code_field=c['measurement'])[0],
                                 polaritytype=PolarityType.objects.filter(type=c['polarity'])[0],
                                 )
        mi.save()

        ss = StudySample.objects.filter(sample_name=c['sample'])[0]


        data_in = {'assay': self.assay.id,
                   'studysample': ss.id,
                   'extractionprocess': ei.id,
                   'speprocess':spei.id,
                   'chromatographyprocess': ci.id,
                   'measurementprocess': mi.id}

        form = AssayDetailForm(data_in)
        form.is_valid()
        ad = form.save()