# core/forms.py
from django import forms
from .models import PlantedTree

class PlantTreeForm(forms.ModelForm):
    plant = forms.CharField(label='Nome da Planta')
     
    class Meta:
        model = PlantedTree
        fields = ('plant', 'latitude', 'longitude')