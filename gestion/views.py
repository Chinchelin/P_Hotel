from django.shortcuts import render
from .models import Cliente
from django.views.generic import ListView 
from django.views.generic.edit import CreateView
from .forms import ClienteForm
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Proveedor
from .forms import ProveedorForm


def tabla_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/tabla_clientes.html', {'clientes': clientes})

# Vista para listar clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/tabla_clientes.html'
    context_object_name = 'clientes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        return context
# Vista para crear nuevo cliente
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/crear.html'
    success_url = '/clientes/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Cliente'
        return context

    def post(self, request, *args, **kwargs):
        print("Se llamó al método POST")
        return super().post(request, *args, **kwargs)

# 

# Vista para editar cliente existente
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/crear.html'
    success_url = '/clientes/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cliente'
        return context

# Vista para eliminar cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/crear.html'  # Usarás el mismo template
    success_url = '/clientes/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Cliente'
        return context
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

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'compras/proveedores.html'
    context_object_name = 'proveedores'

class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'compras/proveedor_form.html'
    success_url = '/proveedores/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Proveedor'
        return context

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'compras/proveedor_form.html'
    success_url = '/proveedores/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Proveedor'
        return context

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'compras/proveedor_form.html'  
    success_url = '/proveedores/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Proveedor'
        return context

# ===============================
# Compras
# ===============================

def compras(request):
    return render(request, 'compras/compras.html')
# ===============================
# Detalle de compras
# ===============================
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
