from django import forms
from .models import Producto, Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductoModelForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0: #con esta validacion nos aseguramos que aparezca un error si el precio es menor a cero.
            raise forms.ValidationError('El precio debe ser mayor que cero. ')
        return precio

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class RegistroUsarioForm(UserCreationForm): 
    email = forms.EmailField(required=True)

    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']