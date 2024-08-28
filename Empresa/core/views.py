from django.shortcuts import render

# Create your views here.

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