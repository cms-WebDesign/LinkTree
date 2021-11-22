from django.shortcuts import render
from django.http import HttpResponse
from .models import cssEditor

# Create your views here.

def index(request):
    editor = cssEditor.objects.get(pk=1)
    return render(
        request,
        "SocialLinks/index.html",
        {
            "linkcolor":editor.link_color,
            "linkfont":editor.link_font,
            "linkbc":editor.link_bc
        }
    )
