from django.shortcuts import render
from .models import Cliente


def tabla_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/tabla_clientes.html', {'clientes': clientes})

# Vista para listar clientes
# Vista para crear nuevo cliente
# Vista para editar cliente existente
# Vista para eliminar cliente
# Vista para ver detalles de un cliente



# ===============================
# Página pública y Login
# ===============================

def pagina(request):
    return render(request, 'pagina/pagina.html')

def login(request):
    return render(request, 'login/login.html')


# ===============================
# Panel de administración
# ===============================

def panel_control(request):
    return render(request, 'panel/panelcontrol.html')


# ===============================
# Usuarios y asignaciones
# ===============================

def usuarios(request):
    return render(request, 'usuarios/usuarios.html')

def asignaciones(request):
    return render(request, 'usuarios/asignaciones.html')


# ===============================
# Clientes
# ===============================

def clientes(request):
    return render(request, 'clientes/clientes.html')


# ===============================
# Hotel: habitaciones, reservas, checkins/outs
# ===============================

def habitaciones(request):
    return render(request, 'hotel/habitaciones.html')

def reservas(request):
    return render(request, 'hotel/reservas/reservas.html')

def detalle_reservas(request):
    return render(request, 'hotel/reservas/detalle_reservas.html')

def checkins(request):
    return render(request, 'hotel/checkins.html')

def checkouts(request):
    return render(request, 'hotel/checkouts.html')


# ===============================
# Inventario
# ===============================

def productos(request):
    return render(request, 'inventario/productos.html')

def categorias(request):
    return render(request, 'inventario/categorias.html')

def marcas(request):
    return render(request, 'inventario/marcas.html')


# ===============================
# Compras
# ===============================

def proveedores(request):
    return render(request, 'compras/proveedores.html')

def compras(request):
    return render(request, 'compras/compras.html')

def detalle_compras(request):
    return render(request, 'compras/detalle_compras.html')


# ===============================
# Ventas
# ===============================

def ventas(request):
    return render(request, 'ventas/ventas.html')

def detalle_ventas(request):
    return render(request, 'ventas/detalle_ventas.html')

def facturas(request):
    return render(request, 'ventas/facturas.html')


# ===============================
# Tareas y Capacitaciones
# ===============================

def tareas(request):
    return render(request, 'tareas/tareas.html')

def capacitaciones(request):
    return render(request, 'capacitaciones/capacitaciones.html')

def asistencias(request):
    return render(request, 'capacitaciones/asistencias.html')


# ===============================
# Reportes
# ===============================

def reportes(request):
    return render(request, 'reportes/reportes.html')
