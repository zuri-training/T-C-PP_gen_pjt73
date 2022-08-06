from django.shortcuts import render
from django.views.generic import TemplateView
from dataclasses import fields
from pyexpat import model
from statistics import mode
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
# Create your views here.




@user_passes_test(lambda u: u.is_superuser)
class PostListView(ListView):
    Model = Post
    
@user_passes_test(lambda u: u.is_superuser)
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    
class PostDetailView(DetailView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    
@user_passes_test(lambda u: u.is_superuser)
class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    
@user_passes_test(lambda u: u.is_superuser)
class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

def homepage(request):
    return render(request, 'blog/index.html')

