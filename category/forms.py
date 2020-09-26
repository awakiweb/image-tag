from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select
from .models import Category


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description', 'parent', 'order', 'level']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'parent': Select(attrs={'class': 'form-control custom-select'}),
            'order': NumberInput(attrs={'class': 'form-control'}),
            'level': NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Nombre de la Categoria',
            'description': 'Descripcion',
            'parent': 'Categoria',
            'order': 'Orden de Aparicion',
            'level': 'Nivel'
        }
