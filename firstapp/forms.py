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


PODFormSet = modelformset_factory(POD, form=PODForm)

# class ADCForm(forms.ModelForm):
#     class Meta:
#         model = cloneInvofjewellery
#         fields = "__all__"


class ADCForm(forms.ModelForm):
    disabled_fields = ['stockid', 'location', 'jewellery_type', 'center_stone', 'shape', 'metal', 'gross_wt',
                       'certificate', 'PCS', 'amount', 'DIS', 'DIS_amount', 'total_value', 'currency', 'tag_price', 'rate']

    class Meta:
        model = cloneInvofjewellery
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ADCForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True

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
