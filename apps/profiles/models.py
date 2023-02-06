from django.db import models
from apps.users.models import User
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
import random
import string
from phone_field import PhoneField

def generate_unique_id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=6, unique=True, default=generate_unique_id)
    first_name = models.CharField(_("First Name"), max_length=50, null=True, blank=True, default="Ivan")
    second_name = models.CharField(_("Second Name"), max_length=50, null=True, blank=True, default="Ivanov")
    last_name = models.CharField(_("Last Name"), max_length=50, null=True, blank=True, default="Ivanovich")
    position = models.CharField("Position", max_length=50, null=True, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    shift_work = models.BooleanField(_("Shift sched?"), default=0)
    # other fields for the profile model, such as bio, location, etc.
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/users/', blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.user.email}'
    
    
    
    
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = generate_unique_id()
        super().save(*args, **kwargs)
        
    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="80" />'.format(self.image.url))
        return ""

    def __str__(self):
        return self.user.get_username()

        
    @property
    def full_name(self):
     return "%s %s %s" % (self.first_name, self.last_name, self.second_name, )