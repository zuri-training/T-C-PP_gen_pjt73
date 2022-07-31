from django.db import models
from django.contrib.auth.models import User
from django.forms import DateTimeField
from django.utils import timezone

# Create your models here.

#only admins can create blog post
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    blog_content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)

#Model for blog comments
class Comment(models.Model):
    blog = models.ForeignKey(Post, on_delete= models.CASCADE)
    content = models.TextField()
    date = DateTimeField()