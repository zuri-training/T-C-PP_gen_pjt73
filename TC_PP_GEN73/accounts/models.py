from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile/pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    #overridding the save method
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        #re-adjusting the size of the user profile image; to save space.
        if img.height > 500 and img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
