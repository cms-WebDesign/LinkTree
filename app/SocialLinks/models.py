from django.db import models

# Create your models here.

class cssEditor(models.Model):
    link_color = models.CharField(max_length=7, default="#000000")
    link_font = models.CharField(max_length=15, default="Brush Script MT")
    link_bc = models.CharField(max_length=7, default="#F5F5F5")

class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

class backgroundImage(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
