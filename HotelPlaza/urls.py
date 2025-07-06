"""
URL configuration for HotelPlaza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')LS
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestion.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panelcontrol/', panel_control,name='panelcontrol'),

    # Usuarios
    path('usuarios/', usuarios,name='usuarios'),

    # clientes
    path('clientes/', clientes,name='clientes'),

    # Habitaciones
    path('habitaciones/', habitaciones,name='habitaciones'),

    # Reservas
    path('reservas/', reservas,name='reservas'),
    path('detalle_reservas/', detalle_reservas,name='detalle_reservas'),
    path('checkins/', checkins,name='checkins'),
    path('checkouts/', checkouts,name='checkouts'),

    # Productos
    path('productos/', productos,name='productos'),
    path('categorias/', categorias,name='categorias'),
    path('marcas/', marcas,name='marcas'),

    # Proveedores y Compras
    path('proveedores/', proveedores,name='proveedores'),
    path('compras/', compras,name='compras'),
    path('detalle_compras/', detalle_compras,name='detalle_compras'),

    # Ventas
    path('ventas/', ventas,name='ventas'),
    path('detalle_ventas/', detalle_ventas,name='detalle_ventas'),
    path('facturas/', facturas,name='facturas'),

    # tareas y Gestión Interna
    path('tareas/', tareas,name='tareas'),
    path('asignaciones/', asignaciones,name='asignaciones'),
    path('capacitaciones/', capacitaciones,name='capacitaciones'),
    path('asistencias/', asistencias,name='asistencias'),

    # reportes
    path('reportes/', reportes,name='reportes'),

    # Login
    path('login/', login,name='login'),


    # Página inicial
    path('', Pagina, name='pagina'),

]
