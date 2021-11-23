from django.contrib import admin
from SocialLinks.forms import *
from .models import Image

# Register your models here.

@admin.register(cssEditor)
class cssEditor(admin.ModelAdmin):
    form = cssForm

admin.site.register(Image)
