from django.forms import ModelForm, TextInput, Textarea, NumberInput
from .models import Category, Subcategory


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description', 'order']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'order': NumberInput(attrs={'class': 'form-control'})
        }

        labels = {
            'name': 'Nombre de la Categoria',
            'description': 'Descripcion',
            'order': 'Orden de Aparicion',
        }

class SubcategoryForm(ModelForm):

    class Meta:
        model = Subcategory
        fields = ['category', 'name', 'description', 'order']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'order': NumberInput(attrs={'class': 'form-control'})
        }

        labels = {
            'category': 'Categoria',
            'name': 'Nombre de la Sub Categoria',
            'description': 'Descripcion',
            'order': 'Orden de Aparicion',
        }
