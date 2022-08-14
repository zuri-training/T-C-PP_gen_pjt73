from urllib import response
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.generic import View, CreateView, FormView
from django.urls import reverse_lazy
from .forms import SignUpForm, ContactLawyer
from django.conf import settings
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .forms import UserUpdateForm, ProfileUpdateForm, BusinessUpdateForm

# Create your views here.

#registration view function
class RegisterView(SuccessMessageMixin,CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('signin')
    template_name = 'accounts/signup.html'
    success_message = "Account successfully. You can now login"

    def get(self, request, *args, **kwargs):
        form = self.form_class(**self.get_form_kwargs())
        return render(request, self.template_name, {'form': form,})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            Password = form.cleaned_data.get('password')
            obj.user = request.user #Assuming that the relevant field is named user, it will save the user accessing the form using request.user
            obj.save()
            messages.success(self.request,f'Account successfully created, you can login now.')
            return redirect('signin')

        else:
            context = {'form': form,}

        return render(request, self.template_name, context)

#login function
def login_view(request):
    if request.method == 'POST':
        #username = request.POST['username']
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        
        else:
            messages.error(request, 'Invalid Credentials. Please Login with the right details.')
            return redirect('signin')
    return render(request, 'accounts/signin.html')



def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required #users can't have access to this view unless they log in
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        b_form = BusinessUpdateForm(request.POST, instance = request.user.profile)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid() and b_form.is_valid():
            u_form.save()
            b_form.save()
            p_form.save()

            messages.success(request, f'Business profile successfully updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        b_form = BusinessUpdateForm(instance=request.user.profile)
        p_form = ProfileUpdateForm(request.FILES, instance=request.user.profile)

        context = {'u_form':u_form, 'b_form':b_form, 'p_form':p_form}
    
    return render(request, 'accounts/profile_page.html', context)


class ContactLawyerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/lawyer.html')

    def post(self,request, *args, **kwargs):
        form = ContactLawyer(request.POST)
        message = request.POST['message']
        if form.is_valid():
            send_mail('Contact Lawyer', message, settings.EMAIL_HOST_USER, ['kadelcode@gmail.com'], fail_silently=False)
            messages.info(request,"Message successfully sent")
            return redirect('contact_dashboard')
        else:
            messages.error(request,'Message not sent due to some reasons. Please ensure you pass in the right message.')
        return render(request, 'accounts/lawyer.html', {'form':form})

'''def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Need a Lawyer', message, settings.EMAIL_HOST_USER, ['kadelcode@gmail.com'], fail_silently=False)
        messages.info(request,"Message successfully sent.")
        return redirect('contact_dashboard')
    else:
        return render(request, 'accounts/lawyer.html')'''

@login_required
def history(request):
    return render(request, 'accounts/history.html')


def forgot(request):
    return render(request, 'accounts/forgot.html')
