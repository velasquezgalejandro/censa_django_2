from django.shortcuts import render
from .models import Cliente, Producto

# Create your views here.
def listar_clientes(request): 
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def listar_productos(request): 
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})