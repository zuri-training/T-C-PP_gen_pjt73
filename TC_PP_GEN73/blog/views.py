from django.shortcuts import render, redirect
from django.views.generic import TemplateView , View
from blog.forms import ContactForm
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
        if form.is_valid():
            return redirect('contact')
        return render(request, 'blog/contact_us.html', {'form':form})

def about(request):
    return render(request, 'blog/about.html')

