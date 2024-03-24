
from django.forms import ModelForm
from django import forms
from .models import Material, gallery

class MaterialForm (ModelForm):
    class Meta:
        model= Material
        fields = "__all__"
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['file', 'course', 'year', 'material_type']
class GalleryForm(forms.ModelForm):
    class Meta:
        model = gallery
        fields = ['event_name', 'poster']
   