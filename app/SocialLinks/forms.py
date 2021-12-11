from django.forms import ModelForm
from django.forms.widgets import TextInput
from SocialLinks.models import *

class cssForm(ModelForm):
    class Meta:
        model = styleEditor
        fields = "__all__"
        widgets = {
            "Link_Color": TextInput(attrs={"type": "color"}),
            "Link_Background_Color": TextInput(attrs={"type": "color"}),
            "Link_Hover_Color": TextInput(attrs={"type": "color"})
        }
