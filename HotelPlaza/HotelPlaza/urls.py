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
    path('panelcontrol/', panel_control),

    # Usuarios
    path('usuarios/', usuarios),

    # Clientes
    path('clientes/', clientes),

    # Habitaciones
    path('habitaciones/', habitaciones),

    # Reservas
    path('reservas/', reservas),
    path('detalle_reservas/', detalle_reservas),
    path('checkins/', checkins),
    path('checkouts/', checkouts),

    # Productos
    path('productos/', productos),
    path('categorias/', categorias),
    path('marcas/', marcas),

    # Proveedores y Compras
    path('proveedores/', proveedores),
    path('compras/', compras),
    path('detalle_compras/', detalle_compras),

    # Ventas
    path('ventas/', ventas),
    path('detalle_ventas/', detalle_ventas),
    path('facturas/', facturas),

    # Tareas y Gestión Interna
    path('tareas/', tareas),
    path('asignaciones/', asignaciones),
    path('capacitaciones/', capacitaciones),
    path('asistencias/', asistencias),

    # Reportes
    path('reportes/', reportes),

    # Login
    path('login/', login),
    # Página inicial
    path('pagina/', Pagina),

]