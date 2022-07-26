from email.policy import default
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


#SIGNUP FORM
class SignUpForm(UserCreationForm):
    class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email = email).count()

        if user_count > 0:
            raise forms.ValidationError('Email already exists.')
        return email

                                    
    def save(self, commit = True):
        user = super(SignUpForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']

        return user

#CONTACT LAWYER FORM
class ContactLawyer(forms.Form):
    message = forms.CharField(widget=forms.Textarea, min_length=30)

    def clean_message(self):
        #actual message you want to validate
        message = self.cleaned_data.get('message')

        if message == "" or message == " ":
            return forms.ValidationError("Field can't be left empty.")

        else:
            return message


'''ModelForm allows users to update their info to the database'''
#Update email and username
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class BusinessUpdateForm(forms.ModelForm):
    business_name = forms.CharField(max_length=30)
    contact = forms.CharField(max_length=12)
    location = forms.CharField(max_length=100)
    class Meta:
        model =  User
        fields = ['business_name', 'contact', 'location']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']