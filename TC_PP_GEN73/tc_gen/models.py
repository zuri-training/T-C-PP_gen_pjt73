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
    

    