#from socket import fromshare 
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length = 200)
    message = forms.CharField(widget=forms.Textarea, min_length=20)