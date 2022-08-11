from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    fields = ['email', 'username', 'password1', 'password2']

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

'''ModelForm allows users to update their info to the database'''
#Update email and username
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']