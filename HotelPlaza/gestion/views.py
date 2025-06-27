# gestion/views.py
from django.shortcuts import render
from django.http import *

# Panel Principal
def panel_control(request):
    return render(request, 'panel/panelcontrol.html')

# Usuarios
def usuarios(request):
    return render(request, 'usuarios.html')

# Clientes
def clientes(request):
    return render(request, 'clientes.html')

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
    return render(request, 'productos.html')

def categorias(request):
    return render(request, 'categorias.html')

def marcas(request):
    return render(request, 'marcas.html')

# Proveedores y Compras
def proveedores(request):
    return render(request, 'proveedores.html')

def compras(request):
    return render(request, 'compras.html')

def detalle_compras(request):
    return render(request, 'detalle_compras.html')

# Ventas
def ventas(request):
    return render(request, 'ventas.html')

def detalle_ventas(request):
    return render(request, 'detalle_ventas.html')

def facturas(request):
    return render(request, 'facturas.html')

# Tareas y Gestión Interna
def tareas(request):
    return render(request, 'tareas.html')

def asignaciones(request):
    return render(request, 'asignaciones.html')

def capacitaciones(request):
    return render(request, 'capacitaciones.html')

def asistencias(request):
    return render(request, 'asistencias.html')

# Reportes
def reportes(request):
    return render(request, 'reportes.html')

# Login
def login(request):
    return render(request, 'login/login.html')

# Página inicial
def Pagina(request):
    return render(request, 'pagina/pagina.html')

def prueba():
    personas = [
        {
            'nombre': 'Juan',
            'edad': 30,
            'email': 'juan@example.com',
        },
        {
            'nombre': 'Ana',
            'edad': 25,
            'email': 'ana@example.com'
        },
    ]
    return personas

def vista3(request):
    personas = prueba()
    return render(request, 'vista3.html', {'personas': personas})
