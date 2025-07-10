from django import forms
from .models import Categoria
# --------------------------------------------
# fromulario: Marca
# --------------------------------------------
class BuscarMarcaForm(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por nombre...'
        })
    )
    
# --------------------------------------------
# fromulario: Categoria
# --------------------------------------------
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Bebidas, Snacks'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción opcional'
            })
        }

class BuscarCategoriaForm(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por nombre...'
        })
    )