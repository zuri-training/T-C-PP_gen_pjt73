from django import forms

from .models import Company


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

    CHOICES = (('yes', 'Yes'), ('no', 'No'))
    cookies = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect())
    google_advertising = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect())
    third_party_advertising = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect())
