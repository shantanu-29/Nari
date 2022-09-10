from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'mobile')

admin.site.register(Profile, ProfileAdmin)
