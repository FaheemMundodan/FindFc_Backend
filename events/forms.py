from django import models
from django.forms import ModelForm
from .models import materials

class MaterialForm (ModelForm):
    class Meta:
        model= materials
        fields = "__all__"
     