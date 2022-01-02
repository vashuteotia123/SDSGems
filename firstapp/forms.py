from django import forms
from django.forms.widgets import Widget
from .models import *
from django.forms import formset_factory, modelformset_factory
from django.contrib.admin.widgets import AdminDateWidget


class CompanyForm(forms.ModelForm):
    class Meta:
        model = companyinfo
        fields = "__all__"


class DateInput(forms.DateInput):
    input_type = "date"


class POJForm(forms.ModelForm):
    class Meta:
        model = POJ
        fields = "__all__"
        labels = {'purchase_approval': 'Bought Jewell'}
        widgets = {'date': DateInput(), 'comment': forms.Textarea(attrs={'rows': 4, 'cols': 30}),
                   'purchase_approval': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px;'})}

        def __init__(self, *args, **kwargs):
            super(POJForm, self).__init__(*args, **kwargs)
            for field in self.disabled_fields:
                self.fields[field].disabled = True
            for field in self.fields:
                if self.fields[field].label == 'Bought Jewell':
                    continue
                self.fields[field].required = True


POJFormSet = modelformset_factory(POJ, form=POJForm)


class POCSForm(forms.ModelForm):
    class Meta:
        model = PurchaseOfColorStones
        fields = "__all__"
        labels = {'purchaseapv': 'Bought Color Stone'}
        widgets = {'date': DateInput(), 'comment': forms.Textarea(attrs={'rows': 4, 'cols': 30}),
                   'purchaseapv': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px;'})}

        def __init__(self, *args, **kwargs):
            super(POCSForm, self).__init__(*args, **kwargs)
            for field in self.disabled_fields:
                self.fields[field].disabled = True
            for field in self.fields:
                if self.fields[field].label == 'Bought Color Stone':
                    continue
                self.fields[field].required = True


POCSFormSet = modelformset_factory(PurchaseOfColorStones, form=POCSForm)


class PODForm(forms.ModelForm):
    class Meta:
        model = POD
        fields = "__all__"
        labels = {'purchaseapv_d': 'Bought Diamond'}
        widgets = {'date': DateInput(), 'comment': forms.Textarea(attrs={'rows': 4, 'cols': 30}),
                   'purchaseapv': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px;'})}

        def __init__(self, *args, **kwargs):
            super(PODForm, self).__init__(*args, **kwargs)
            for field in self.disabled_fields:
                self.fields[field].disabled = True
            for field in self.fields:
                if self.fields[field].label == 'Bought Diamond':
                    continue
                self.fields[field].required = True


PODFormSet = modelformset_factory(POD, form=PODForm)

# class ADCForm(forms.ModelForm):
#     class Meta:
#         model = cloneInvofjewellery
#         fields = "__all__"


class ADCForm(forms.ModelForm):
    disabled_fields = ['stockid', 'location', 'jewellery_type',
                       'center_stone', 'color_of_center_stone', 'shape', 'metal', 'certificate']

    class Meta:
        model = cloneInvofjewellery
        fields = '__all__'
        labels = {'salesapprovalstatus': 'Sold Item', }

    def __init__(self, *args, **kwargs):
        super(ADCForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True
        for field in self.fields:
            if self.fields[field].label == 'Sold Item':
                continue
            self.fields[field].required = True


ADCFormSet = modelformset_factory(cloneInvofjewellery, form=ADCForm, extra=0)


class ADCForm_cs(forms.ModelForm):
    disabled_fields = ['stockid', 'location', 'shape', 'gem_type', 'origin', 'treatment',
                       'certificate_no', 'color', 'measurements', 'lab', 'Clarity']

    class Meta:
        model = cloneInvofcolorstones
        fields = '__all__'
        labels = {'salesapprovalstatus_cs': 'Sold Item', }

    def __init__(self, *args, **kwargs):
        super(ADCForm_cs, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True
        for field in self.fields:
            if self.fields[field].label == 'Sold Item' or self.fields[field].label == 'Clarity':
                continue
            self.fields[field].required = True


ADCFormSet_cs = modelformset_factory(
    cloneInvofcolorstones, form=ADCForm_cs, extra=0)


class ADCForm_d(forms.ModelForm):
    disabled_fields = ['stockid', 'location', 'shape', 'white_color_grade1', 'fancycolor_grade', 'cut', 'polish', 'symmetry',
                       'measurements', 'depth', 'table', 'fluorescence_intensity', 'fluorescence_color', 'certificate_no_d', 'certificate_d', 'laser_inscription', 'color_origin1', 'clarity', 'units']

    class Meta:
        model = cloneInvofdiamond
        fields = '__all__'
        labels = {'salesapprovalstatus_d': 'Sold Item',
                  'white_color_grade1': 'white_color_grade1',
                  'laser_inscription': 'laser_inscription', }

    def __init__(self, *args, **kwargs):
        super(ADCForm_d, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True
        for field in self.fields:
            if self.fields[field].label == "Sold Item" or self.fields[field].label == 'white_color_grade1' or self.fields[field].label == 'laser_inscription':
                continue
            self.fields[field].required = True


ADCFormSet_d = modelformset_factory(cloneInvofdiamond, form=ADCForm_d, extra=0)


class contactformemail(forms.Form):
    fromemail = forms.EmailField(max_length=150, required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000, required=True)
