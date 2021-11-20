from django.contrib import admin
from SocialLinks.forms import *

# Register your models here.

@admin.register(cssEditor)
class cssEditor(admin.ModelAdmin):
    form = cssForm
