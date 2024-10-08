from django import forms
from django.forms import ModelForm
from .models import *

# Crear un template para poder usarlo en el html
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'tipo', 'description', 'precio']