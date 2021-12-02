from django import forms
from django.forms.widgets import Widget
from .models import *
from django.forms import formset_factory, modelformset_factory
from django.contrib.admin.widgets import AdminDateWidget


class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    disabled_fields = ['permit_user']

    class Meta:
        model = User_table
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
            'permit_user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True

    def clean(self):
        cleaned_data = super(UserForm, self).clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                self.add_error(
                    'password', "The two password fields must match.")
                raise forms.ValidationError("")
        return cleaned_data


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
        widgets={'date': DateInput(), 'comment': forms.Textarea(attrs={'rows': 4, 'cols': 30}),
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
    disabled_fields=['stockid','location','jewellery_type','center_stone','color_of_center_stone','shape','metal','certificate']

    class Meta:
        model = cloneInvofjewellery
        fields = '__all__'
        labels={'salesapprovalstatus':'Sold Item',}
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
                       'certificate_no', 'color', 'measurements', 'lab', 'Weight_cs','Clarity']

    class Meta:
        model = cloneInvofcolorstones
        fields = '__all__'
        labels = {'salesapprovalstatus_cs': 'Sold Item', }

    def __init__(self, *args, **kwargs):
        super(ADCForm_cs, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True
        for field in self.fields:
            if self.fields[field].label == 'Sold Item':
                continue
            self.fields[field].required = True


ADCFormSet_cs = modelformset_factory(
    cloneInvofcolorstones, form=ADCForm_cs, extra=0)


class ADCForm_d(forms.ModelForm):
    disabled_fields = ['stockid', 'location', 'shape', 'clarity', 'white_color_grade1', 'fancycolor_grade', 'cut', 'polish', 'symmetry',
                       'measurements', 'depth', 'table', 'fluorescence_intensity', 'fluorescence_color', 'certificate_no_d', 'certificate_d', 'laser_inscription', 'PCS_d']

    class Meta:
        model = cloneInvofdiamond
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ADCForm_d, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True
        for field in self.fields:
            self.fields[field].required = True



ADCFormSet_d = modelformset_factory(cloneInvofdiamond, form=ADCForm_d, extra=0)


class contactformemail(forms.Form):
    fromemail = forms.EmailField(max_length=150, required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000, required=True)
