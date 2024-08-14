from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import ProductoModelForm, ClienteModelForm

# Create your views here.
def listar_clientes(request): 
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def listar_productos(request): 
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def agregar_producto(request): 
    if request.method == 'POST':
        form = ProductoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoModelForm
        return render(request, 'agregar_producto.html', {'form': form})
        
def agregar_cliente(request): 
    if request.method == 'POST':
        form = ClienteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteModelForm
        return render(request, 'agregar_cliente.html', {'form': form})

def inicio(request):
    return render(request, 'inicio.html')