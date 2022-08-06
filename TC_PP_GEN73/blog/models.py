from django.db import models
from django.contrib.auth.models import User
from django.forms import DateTimeField
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

from TC_PP_GEN73.blog import admin
# Create your models here.


class Post(models.Model):

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    # DB Fields
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, unique=True, editable=False)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft"
    )

    class Meta:
        ordering = ("-publish",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        pass 

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

                    #only admins can create blog post
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=30)
#     blog_content = models.TextField()
#     date_posted = models.DateTimeField(default = timezone.now)

#Model for blog comments
class Comment(models.Model):
    blog = models.ForeignKey(Post, on_delete= models.CASCADE)
    content = models.TextField()
    date = DateTimeField()