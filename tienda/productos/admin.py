# Register your models here.
from django.contrib import admin
from .models import Cliente, Producto


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre', 'email', 'telefono')
    ordering = ('id', )


@admin.register(Producto)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio')
    search_fields = ('nombre', 'precio')
    ordering = ('id', )