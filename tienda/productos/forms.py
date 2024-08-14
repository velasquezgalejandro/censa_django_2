from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    stock = forms.IntegerField()

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.CharField(widget=forms.Textarea)
    telefono = forms.DecimalField(max_digits=10, decimal_places=2)
