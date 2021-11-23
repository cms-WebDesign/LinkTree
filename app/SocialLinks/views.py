from django.shortcuts import render
from django.http import HttpResponse
from .models import cssEditor, Image, backgroundImage

# Create your views here.

def index(request):
    editor = cssEditor.objects.get(pk=1)
    imageModel = Image.objects.get(pk=1)
    backgroundModel = backgroundImage.objects.get(pk=1)

    return render(
        request,
        "SocialLinks/index.html",
        {
            "linkcolor":editor.link_color,
            "linkfont":editor.link_font,
            "linkbc":editor.link_bc,
            "profile_pic_title":imageModel.title,
            "profile_pic":imageModel.image,
            "background_pic_title":backgroundModel.title,
            "background_pic":backgroundModel.image
        }
    )
