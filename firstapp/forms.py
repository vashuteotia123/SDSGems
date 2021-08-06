from django import forms
from .models import *

# class CompanyForm(forms.ModelForm):
#     class Meta:
#         model = companyinfo
#         fields = "__all__"
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
