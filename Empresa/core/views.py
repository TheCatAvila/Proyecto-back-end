from django.shortcuts import render
from .models import *

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
    return render(request, 'core/productos/add.html')