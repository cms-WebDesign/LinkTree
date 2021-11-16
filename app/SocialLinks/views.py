from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
        template = loader.get_template("SocialLinks/index.html")
        return HttpResponse(template.render)
