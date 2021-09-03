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

class POCSForm(forms.ModelForm):
    class Meta:
        model = PurchaseOfColorStones
        fields = "__all__"

class PODForm(forms.ModelForm):
    class Meta:
        model = POD
        fields = "__all__"


# class ADCForm(forms.ModelForm):
#     class Meta:
#         model = cloneInvofjewellery
#         fields = "__all__"

class ADCForm(forms.ModelForm):
    disabled_fields = ['stockid','location','jewellery_type','center_stone','shape','metal','gross_wt','certificate','PCS','amount','DIS','DIS_amount','total_value','currency','tag_price','rate']

    class Meta:
        model = cloneInvofjewellery
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ADCForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True
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

ADCFormSet = modelformset_factory(cloneInvofjewellery,form = ADCForm, extra = 0)
