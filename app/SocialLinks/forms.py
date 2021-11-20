from django.forms import ModelForm
from django.forms.widgets import TextInput
from SocialLinks.models import *

class cssForm(ModelForm):
    class Meta:
        model = cssEditor
        fields = "__all__"
        widgets = {
            "link_color": TextInput(attrs={"type": "color"}),
            "link_bc": TextInput(attrs={"type": "color"})
        }
