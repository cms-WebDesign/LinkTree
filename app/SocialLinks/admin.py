from django.contrib import admin
from SocialLinks.forms import *
from .models import Image, backgroundImage

# Register your models here.

@admin.register(cssEditor)
class cssEditor(admin.ModelAdmin):
    form = cssForm

admin.site.register(Image)
admin.site.register(backgroundImage)
