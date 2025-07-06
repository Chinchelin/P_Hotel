# gestion/views.py
from django.shortcuts import render
from django.http import *

# Panel Principal
def panel_control(request):
    return render(request, 'panel/panelcontrol.html')

# Usuarios
def usuarios(request):
    return render(request, 'usuarios/usuarios.html')

# clientes
def clientes(request):
    return render(request, 'clientes/clientes.html')

# Habitaciones
def habitaciones(request):
    return render(request, 'hotel/habitaciones.html')

# Reservas
def reservas(request):
    return render(request, 'hotel/reservas/reservas.html')

def detalle_reservas(request):
    return render(request, 'hotel/reservas/detalle_reservas.html')

def checkins(request):
    return render(request, 'hotel/checkins.html')

def checkouts(request):
    return render(request, 'hotel/checkouts.html')

# Productos
def productos(request):
    return render(request, 'inventario/productos.html')

def categorias(request):
    return render(request, 'inventario/categorias.html')

def marcas(request):
    return render(request, 'inventario/marcas.html')

# Proveedores y Compras
def proveedores(request):
    return render(request, 'compras/proveedores.html')

def compras(request):
    return render(request, 'compras/compras.html')

def detalle_compras(request):
    return render(request, 'compras/detalle_compras.html')

# Ventas
def ventas(request):
    return render(request, 'ventas/ventas.html')

def detalle_ventas(request):
    return render(request, 'ventas/detalle_ventas.html')

def facturas(request):
    return render(request, 'ventas/facturas.html')

# tareas y Gestión Interna
def tareas(request):
    return render(request, 'tareas/tareas.html')

def asignaciones(request):
    return render(request, 'usuarios/asignaciones.html')

def capacitaciones(request):
    return render(request, 'capacitaciones/capacitaciones.html')

def asistencias(request):
    return render(request, 'capacitaciones/asistencias.html')

# reportes
def reportes(request):
    return render(request, 'reportes/reportes.html')

# Login
def login(request):
    return render(request, 'login/login.html')

# Página inicial
def Pagina(request):
    return render(request, 'pagina/pagina.html')
