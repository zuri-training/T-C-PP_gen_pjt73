from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    business_name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    contact = models.CharField(max_length=12)
    location = models.CharField(max_length=100)
    image = models.ImageField(default = 'user-circle.png', upload_to = 'profile/pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    #overridding the save method
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        #re-adjusting the size of the user profile image; to save space.
        if img.height > 500 and img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
