from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def whoarewe(request):
    return render(request, 'core/whoarewe.html')