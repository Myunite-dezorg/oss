from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

# @receiver(post_save, sender=User)
# def add_user_to_default_group(sender, instance, created, **kwargs):
#     if created:
#         default_group = Group.objects.get(name='default')
#         instance.groups.add(default_group)