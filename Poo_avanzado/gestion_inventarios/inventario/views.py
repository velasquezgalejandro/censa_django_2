from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Proveedor, DetalleProducto
from .forms import ProductoForm, CategoriaForm, ProveedorForm, DetalleProductoForm

# Create your views here.

def inicio(request):
    return render(request, 'inventario/inicio.html')


def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/listar_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        detalle_form =  DetalleProductoForm(request.POST)
        if producto_form.is_valid() and detalle_form.is_valid():
            producto = producto_form.save()
            detalle = detalle_form.save(commit=False)
            detalle.producto = producto
            detalle.save()
            return redirect('listar_productos')
    else: 
        producto_form = ProductoForm()
        detalle_form = DetalleProductoForm()
    return render(request, 'inventario/agregar_producto.html', {'producto_form': producto_form , 'detalle_form': detalle_form})

        

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_producto')
    return render(request, 'inventario/eliminar_producto.html', {'producto': producto})

# Vistas para Categoria
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'inventario/listar_categorias.html', {'categorias': categorias})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'inventario/agregar_categorias.html', {'form': form})

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'inventario/editar_categoria.html', {'form': form})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'inventario/eliminar_categoria.html', {'categoria': categoria})

# Vistas para Proveedor
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'inventario/listar_proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'inventario/agregar_proveedor.html', {'form': form})

def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'inventario/editar_proveedor.html', {'form': form})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listar_proveedores')
    return render(request, 'inventario/eliminar_proveedor.html', {'proveedor': proveedor})


