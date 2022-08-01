from django.shortcuts import render, redirect
from .forms import UserRegisterForm
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