from django.urls import path
from .views import listar_clientes, listar_productos, agregar_cliente, agregar_producto

urlpatterns = [
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('productos/', listar_productos, name='listar_productos'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('agregar-cliente/', agregar_cliente, name='agregar_cliente'),
]