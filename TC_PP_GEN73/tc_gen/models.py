from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

RATING_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)

class Lawyer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    lawyer = models.ForeignKey(Lawyer, on_delete= models.CASCADE)
    phone_number = models.CharField(max_length=12)


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ratings = models.IntegerField(choices=RATING_CHOICES, default=1)
    

    #Creating model for company data-mariam &jude
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    company_website_name = models.CharField(max_length=50)
    company_website_url = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    company_email_address = models.EmailField(max_length=50)

    def __str__(self):
        return self.company_name


#Creating model for template auto fill(Mariam & Jude)
class Template(models.Model):
    company = models.ForeignKey(Company, on_delete = models.PROTECT)
    slug = models.SlugField()

    def __str__(self):
        return self.company.company_name