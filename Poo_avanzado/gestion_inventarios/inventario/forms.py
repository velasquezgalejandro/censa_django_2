from django import forms
from .models import Producto, Categoria, Proveedor, DetalleProducto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'proveedor', 'etiquetas', 'cantidad', 'precio', 'descripcion']

    def clena_precio(self):

        precio = self.cleaned_data.get('precio')
        if precio < 0:
            raise forms.ValidationError('El precio no pude ser negativo')
        return precio

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre: 
            raise forms.ValidationError('El nombre no pude quedar vacio')
        return nombre

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'telefono']

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit():
            raise forms.ValidationError('El numero de telefono debe contener solo digitos.')
        return telefono

class DetalleProductoForm(forms.ModelForm):
    class Meta:
        model = DetalleProducto
        fields = ['espicificaciones', 'fecha_vencimiento']