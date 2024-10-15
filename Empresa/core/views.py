from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def about(request):
    return render(request, 'core/about.html')

def cart(request):
    return render(request, 'core/cart.html')

def blog(request):
    return render(request, 'core/blog.html')

# CRUD
def listProductos(request):
    # SELECT * FROM empleados
    listaProductos = Producto.objects.all()
    datos = {
        'listaProductos':listaProductos
    }

    return render(request, 'core/productos/list.html', datos)

def addProducto(request):
    datos = {
        'form':ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['msj'] = "Producto Guardado correctamente"
    
    return render(request, 'core/productos/add.html', datos)

def updateProducto(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form':ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['msj'] = "Producto Actualizados correctamente"
            datos['form'] = formulario
    
    return render(request, 'core/productos/update.html', datos)

def deleteProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    
    return redirect(to="listProductos")