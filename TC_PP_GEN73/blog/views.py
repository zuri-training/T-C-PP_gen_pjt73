from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def homepage(request):
    return render(request, 'blog/index.html')

