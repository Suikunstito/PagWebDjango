from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from .views import index, registro, ingresar, salir, nosotros, productos, ficha, usuarios, bodega
from .views import eliminar_producto_en_bodega, ventas, misdatos, miscompras, carrito, agregar_producto_al_carrito
from .views import eliminar_producto_en_carrito, ropa

urlpatterns = [
    path('', index, name='index'),
    path('registro', registro, name='registro'),
    path('ingresar', ingresar, name='ingresar'),
    path('salir', salir, name='salir'),
    path('nosotros', nosotros, name='nosotros'),
    path('productos/<accion>/<id>', productos, name='productos'),
    path('ficha/<producto_id>', ficha, name='ficha'),
    path('usuarios/<accion>/<id>', usuarios, name='usuarios'),
    path('bodega', bodega, name='bodega'),
    path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),
    path('ventas', ventas, name='ventas'),
    path('misdatos', misdatos, name='misdatos'),
    path('miscompras', miscompras, name='miscompras'),
    path('carrito', carrito, name='carrito'),
    path('agregar_producto_al_carrito/<producto_id>', agregar_producto_al_carrito, name='agregar_producto_al_carrito'),
    path('eliminar_producto_en_carrito/<carrito_id>', eliminar_producto_en_carrito, name='eliminar_producto_en_carrito'),
    path('ropa', ropa, name="ropa"),
]