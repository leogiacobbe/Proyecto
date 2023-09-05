from django.shortcuts import render, redirect
from .models import Producto
from django.views.generic.detail import DetailView

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto.html', {'productos': productos})

def insertar_producto(request):
    if request.method == 'POST':
        id = request.POST['id']
        nombre = request.POST['nombre']
        imagen1 = request.POST['imagen1']
        precio = request.POST['precio']
        producto = Producto(id=id, nombre=nombre, imagen1=imagen1, precio=precio)
        producto.save()
        return redirect('listar_productos')

    return listar_productos(request)

def editar_producto(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.imagen1 = request.POST['imagen1']
        producto.precio = request.POST['precio']
        producto.save()
        return redirect('listar_productos')
    return render(request, 'editar_producto.html', {'producto': producto})

def eliminar_producto(request, pk):
    producto = Producto.objects.get(id=pk)
    producto.delete()
    return redirect('listar_productos')

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'detalle_producto.html'
    context_object_name = 'producto'