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