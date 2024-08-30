repositorio para poo avanzado 

29/08/2024

Relaciones one to many 
relacion donde un registro de la tabla se puede asociar a multiples registros en las siguientes tablas
pero cada registro de la otra tabla esta relacionado a un solo registro

categoria mouse == muchos mouses 
muchos mouses == categoria mouse 

relaciones many to many
multiples registros se conectan a multiples registros de otra table 
relaciones multiples entre si 
categoria mouse, categoria gamer == muchos mouses gamers 
muchos mouses gamers == categoria mouse , caregoria gamer

def editar_producto(request, pk):
    producto = Producto.objects.get(pk=pk) #Se selciona el producto con el primary key que llega desde arriba
    if request.method == 'POST' #se mantiene metodo post para la actualizacion 
        form = ProductoForm(request.Post, instance=producto) # se toma la instancia para tener los datos del producto
        if form is_valid() # validacion
            form.save
            return redirect()
    else 
        form = ProductoForm(instance=producto) # lo mismo de los datos para mantener
        return render(reques, 'html', {form: form}) #renderiza vista

en urls 

path('productos/editar/<int:pk>', editar_producto, name='editar_producto') #para las que necesiten p