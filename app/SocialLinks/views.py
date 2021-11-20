from django.shortcuts import render
from django.http import HttpResponse
from .models import cssEditor

# Create your views here.

def index(request):
    linkcolor = "#000"
    linkfont = "Brush Script MT"
    linkbc = "whitesmoke"
    return render(request, "SocialLinks/index.html", {"linkcolor":linkcolor, "linkfont":linkfont, "linkbc":linkbc})
