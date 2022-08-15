import email
from django.shortcuts import render, redirect
from django.views.generic import TemplateView , View
from blog.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def homepage(request):
    return render(request, 'blog/index.html')

def service(request):
    return render(request, 'blog/service.html')

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/contact_us.html')

    def post(self,request, *args, **kwargs):
        form = ContactForm(request.POST)
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST.get('email')
        if form.is_valid():
            send_mail(subject, message, email , ['kadelcode@gmail.com'], fail_silently=False)#settings.EMAIL_HOST_USER
            messages.info(request,"Message successfully sent. We'll respond to you within 24 hours.")
            return redirect('contact')
        return render(request, 'blog/contact_us.html', {'form':form})

def about(request):
    return render(request, 'blog/about.html')

