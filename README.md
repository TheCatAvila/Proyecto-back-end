# Clases-Back-end
https://themewagon.com/

PASOS:

1. Instalar miniconda. (Recordar el PATH)
2. Instalar django
    pip install django
3. Crear proyecto
    django-admin startproject NOMBREPROYECTO
4. Craer APP 
    python manage.py startapp NOMBREAPP (app o core)
5. para iniciar el proyecto:
    python manage.py runserver

PASOS 2: 

1. crear base.html en templates/core
    {% block principal %}

    {% endblock %}
2. configurar el contenido(lo que se herada)
3. configurar cada una de las paginas:
    index, contacto, quienes somos

PASOS 3:

1. models.py: se declaran los modelos
2. terminal: 
    -crear el script:
    -python manage.py makemigrations
    -Migra el script hacia la BD:
        -python manage.py migrate
3. configurar el administrador:
    -Crear un superuser:
        -python manage.py createsuperuser

4. admin.py: agrega los modelos

5. urls.py principal: puede cambiar los titulos del admin:
    # Confoguración del admin
    admin.site.site_title  = 'tittle'
    admin.site.site_header = 'header'
    admin.site.index_title = 'index_title'

6. apps.py: Agregar:
    verbose_name = 'verbose_name'

7. Para arreglar el objeto del admin:
    -models.py:
    def __str__(self):
        return self.name

8. admin.py: configurar en formato tabla los modelos

Pasos 4

1. Crear las views:
    -add, update, delete, list, find, etc.

2. Crear las vistas para cada View:
    templates/core/empleados/add
    templates/core/empleados/update
    templates/core/empleados/list

3. Crear los templates forms para los formularios:
    - crear un archivo llamado forms.py

4. Configurar todas las urls en urls.py

5. Configurar los enlaces en el base

-------------------------------------------------------

django-admin startproject proyecto2
cd proyecto2
python manage.py startapp core
python manage.py runserver

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index" ),
]

{% load static %}
{% static 'core/ ' %}

{% extends 'core/base.html' %}
{% url 'login' %}