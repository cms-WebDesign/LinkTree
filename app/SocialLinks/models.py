from django.db import models

# Create your models here.

class styleEditor(models.Model):
    Title = models.CharField(max_length=20, default="Home")
    Link_Color = models.CharField(max_length=7, default="#000000")
    Link_Font_Style = models.CharField(max_length=15, default="Brush Script MT")
    Link_Background_Color = models.CharField(max_length=7, default="#F5F5F5")
    Link_Hover_Color = models.CharField(max_length=7, default="#000000")

class profilePic(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

class backgroundPic(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

class links(models.Model):
    link1 = models.CharField(max_length=100, default="https://www.instagram.com")
    link2 = models.CharField(max_length=100, default="https://www.facebook.com")
    link3 = models.CharField(max_length=100, default="https://www.namecheap.com")
    link4 = models.CharField(max_length=100, default="mailto:email@gmail.com")
    link5 = models.CharField(max_length=100, default="https://www.contactme.com")
    link6 = models.CharField(max_length=100, default="https://www.link6.com")
    link7 = models.CharField(max_length=100, default="https://www.link7.com")
