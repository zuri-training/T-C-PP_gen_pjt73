from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def homepage(request):
    return render(request, 'blog/index.html')

def service(request):
    return render(request, 'blog/service.html')

def contact(request):
    return render(request, 'blog/contact_us.html')

def about(request):
    return render(request, 'blog/about.html')
