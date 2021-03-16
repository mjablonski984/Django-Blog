from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# import signals in apps.py
# Create Profile automatcally when User is created
@receiver(post_save, sender=User) # when User is saved send post_save signal
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save created Profile for  a user
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()