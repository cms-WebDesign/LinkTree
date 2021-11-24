from django.shortcuts import render
from django.http import HttpResponse
from .models import styleEditor, profilePic, backgroundPic

# Create your views here.

def index(request):
    editor = styleEditor.objects.get(pk=1)
    imageModel = profilePic.objects.get(pk=1)
    backgroundModel = backgroundPic.objects.get(pk=1)

    return render(
        request,
        "SocialLinks/index.html",
        {
            "web_title":editor.Title,
            "linkcolor":editor.Link_Color,
            "linkfont":editor.Link_Font_Style,
            "linkbc":editor.Link_Background_Color,
            "link_hover_color":editor.Link_Hover_Color,
            "profile_pic_title":imageModel.title,
            "profile_pic":imageModel.image,
            "background_pic_title":backgroundModel.title,
            "background_pic":backgroundModel.image
        }
    )
