from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    #set the help text of fields to none
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email Address'
        self.fields['password2'].label = 'Confirm Password'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User #form data will be saved in the User model
        fields = ['email','username','password1','password2'] #field required for registration

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