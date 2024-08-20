from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'), #PÁGINA DE INICIO
    path('contacto/', contacto, name='contacto'), #PÁGINA DE CONTACTO
    path('whoarewe/', whoarewe, name='whoarewe'), #PÁGINA DE QUIENES SOMOS
]