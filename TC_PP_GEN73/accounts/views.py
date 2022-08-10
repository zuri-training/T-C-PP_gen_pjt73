from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

#registration view function
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Succesfully created for {username}!')

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register_page.html',{'form':form})

# @login_required #users can't have access to this view unless they log in
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def profile(request):
    return render(request, 'accounts/profile_page.html')

def contact(request):
    return render(request, 'accounts/lawyer.html')

def history(request):
    return render(request, 'accounts/history.html')