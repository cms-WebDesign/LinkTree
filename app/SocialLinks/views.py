from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    linkcolor = "#000"
    font = "Brush Script MT"
    return render(request, "SocialLinks/index.html", {"linkcolor":linkcolor, "font":font})
