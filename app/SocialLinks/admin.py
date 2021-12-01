from django.contrib import admin
from SocialLinks.forms import *
from .models import profilePic, backgroundPic, styleEditor

# Register your models here.

@admin.register(styleEditor)
class styleEditor(admin.ModelAdmin):
    form = cssForm

admin.site.register(profilePic)
admin.site.register(backgroundPic)
admin.site.register(links)
