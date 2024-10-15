from django.urls import path
from .views import *


#LAS URLS SIRVEN PARA LLAMAR A LAS PÁGINAS

urlpatterns = [
    path('', index, name='index'), #PÁGINA DE INICIO
    path('contacto/', contacto, name='contacto'), #PÁGINA DE CONTACTO
    path('about/', about, name='about'), #PÁGINA DE QUIENES SOMOS
    path('cart/', cart, name='cart'), #PÁGINA DEL CARRITO
    path('blog/', blog, name='blog'), #PÁGINA DEL CARRITO
    # CRUD PRODUCTOS
    path('productos/', listProductos, name='listProductos'), # LISTAR PRODUCTOS
    path('add-producto/', addProducto, name='addProducto'), # ADD PRODUCTOS
    path('updateProducto/<id>/', updateProducto, name='updateProducto'), # UPDATE PRODUCTOS
    path('deleteProducto/<id>/', deleteProducto, name='deleteProducto'), # DELETE PRODUCTOS
]