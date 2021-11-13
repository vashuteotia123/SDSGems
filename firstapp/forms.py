from django import forms
from .models import *
from django.forms import formset_factory, modelformset_factory


class CompanyForm(forms.ModelForm):
    class Meta:
        model = companyinfo
        fields = "__all__"


class POJForm(forms.ModelForm):
    class Meta:
        model = POJ
        fields = "__all__"



POJFormSet = modelformset_factory(POJ, form=POJForm)


class POCSForm(forms.ModelForm):
    class Meta:
        model = PurchaseOfColorStones
        fields = "__all__"


POCSFormSet = modelformset_factory(PurchaseOfColorStones, form=POCSForm)


class PODForm(forms.ModelForm):
    class Meta:
        model = POD
        fields = "__all__"
    class DateForm(forms.Form):
        date = forms.DateTimeField(
            input_formats=['%m-%d-%Y'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        )

PODFormSet = modelformset_factory(POD, form=PODForm)

# class ADCForm(forms.ModelForm):
#     class Meta:
#         model = cloneInvofjewellery
#         fields = "__all__"


class ADCForm(forms.ModelForm):

    class Meta:
        model = cloneInvofjewellery
        fields = '__all__'


    # def save(self, *args, **kwargs):
    #     new_obj = Salesofjewellery.objects.create(stockid=self.stockid, company_name=self.company_name, location=self.location, jewellery_type=self.jewellery_type,
    #                                               center_stone=self.center_stone, shape=self.shape,
    #                                               metal=self.metal, gross_wt=self.gross_wt, certificate=self.certificate, PCS=self.PCS, amount=self.amount, DIS=self.DIS, DIS_amount=self.DIS_amount, total_value=self.total_value, currency=self.currency, tag_price=self.tag_price,
    #                                               rate=self.rate, salesapprovalstatus=self.salesapprovalstatus)
        # class cloneJForm(forms.ModelForm):
        #     class Meta:
        #         model = cloneInvofjewellery
        #         fields = "__all__"
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)

        #     self.fields['currency'].queryset = Currency.objects.none()

        #     if 'company_name' in self.data:
        #         try:
        #             company_id = self.data.get('company_name')
        #             curr_company = companyinfo.objects.get(company_id=company_id)
        #             country_now = curr_company.country
        #             self.fields['currency'].queryset = Currency.objects.filter(country = country_now)
        #         except(ValueError, TypeError):
        #             pass
        #     else:
        #         self.fields['currency'].queryset = Currency.objects.all()


ADCFormSet = modelformset_factory(cloneInvofjewellery, form=ADCForm, extra=0)


class ADCForm_cs(forms.ModelForm):
    # disabled_fields = ['stockid', 'location', 'shape', 'gem_type', 'origin', 'treatment',
    #                    'certificate_no', 'color', 'measurements', 'lab', 'Weight_cs', 'amount_cs', 'DIS_cs', 'DIS_amount_cs', 'total_value_cs', 'currency_cs']

    class Meta:
        model = cloneInvofcolorstones
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(ADCForm_cs, self).__init__(*args, **kwargs)
    #     for field in self.disabled_fields:
    #         self.fields[field].disabled = True


ADCFormSet_cs = modelformset_factory(
    cloneInvofcolorstones, form=ADCForm_cs, extra=0)


class ADCForm_d(forms.ModelForm):
    disabled_fields = ['stockid', 'location', 'shape', 'clarity', 'white_color_grade1', 'fancy_color_intensity1', 'fancycolor_grade', 'cut', 'polish', 'symmetry',
                       'measurements', 'depth', 'table', 'fluorescence_intensity', 'fluorescence_color', 'certificate_no_d', 'certificate_d', 'laser_inscription', 'PCS_d', 'weight_d',
                       'amount_d', 'DIS_d', 'DIS_Amount_d', 'total_value_d', 'currency']

    class Meta:
        model = cloneInvofdiamond
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ADCForm_d, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True


ADCFormSet_d = modelformset_factory(cloneInvofdiamond, form=ADCForm_d, extra=0)

class contactformemail(forms.Form):
    fromemail = forms.EmailField(max_length = 150,required=True)
    subject= forms.CharField(required=True)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000,required=True)