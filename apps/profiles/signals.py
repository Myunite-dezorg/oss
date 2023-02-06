from django.db.models.signals import post_save
from apps.users.models import User
from .models import Profile
from django.dispatch import receiver
import string
import random

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
        

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
#         Profile.objects.create(user=instance, unique_id=unique_id)