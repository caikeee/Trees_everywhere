# forms.py
from django import forms
from .models import PlantedTree, Tree

class PlantTreeForm(forms.ModelForm):
    tree = forms.ModelChoiceField(queryset=Tree.objects.all(), label='Árvore', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = PlantedTree
        fields = ['tree', 'age', 'location_lat', 'location_long']



