from logging import PlaceHolder
from socket import fromshare
from django import forms
from .models import Company

class WebsiteForm(forms.ModelForm):
    class Meta:
       model = Company
       fields = '__all__'

    class SaveTermsForm(forms.Form):
        company_name = forms.CharField(max_length=50)