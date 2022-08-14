from django.db.models.signals import post_save #post_save signal is fired after an object is saved to the db
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile # A profile will be created for a new user

#create profile function
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        #create a profile object
        Profile.objects.create(user = instance)

#save profile function
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()