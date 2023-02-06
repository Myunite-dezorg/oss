from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from .models import Profile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'unique_id', 'profile_link')

    def profile_link(self, obj):
        url = reverse('profiles:detail', args=[obj.unique_id])
        return format_html('<a href="{}">View profile</a>'.format(url))
    profile_link.short_description = 'Profile'

admin.site.register(Profile, UserProfileAdmin)