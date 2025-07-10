from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Usuario, Habitacion, Capacitacion
from .forms import UsuarioForm, HabitacionForm, CapacitacionForm

# ===============================
# Vistas básicas (funciones)
# ===============================
def pagina(request):
    """Vista para la página de inicio pública"""
    return render(request, 'pagina/pagina.html')

def login(request):
    """Vista para el login"""
    return render(request, 'login/login.html')

def panel_control(request):
    """Vista para el panel de control"""
    return render(request, 'panel/panelcontrol.html')

def clientes(request):
    """Vista para la sección de clientes"""
    return render(request, 'clientes/clientes.html')

def tabla_clientes(request):
    """Vista para la tabla de clientes"""
    return render(request, 'clientes/tabla_clientes.html')

def reservas(request):
    """Vista para reservas"""
    return render(request, 'reservas/reservas.html')

# ===============================
# Vistas para Usuarios (clases)
# ===============================
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/lista_usuarios.html'
    context_object_name = 'usuarios'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Usuarios'
        context['crear_url'] = reverse_lazy('usuario_crear')
        context['entidad'] = 'Usuarios'
        return context

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/form_usuario.html'
    success_url = reverse_lazy('usuario_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Nuevo Usuario'
        context['listar_url'] = reverse_lazy('usuario_lista')
        context['entidad'] = 'Usuarios'
        return context

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/form_usuario.html'
    success_url = reverse_lazy('usuario_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Usuario'
        context['listar_url'] = reverse_lazy('usuario_lista')
        context['entidad'] = 'Usuarios'
        return context

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar_usuario.html'
    success_url = reverse_lazy('usuario_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Usuario'
        context['listar_url'] = reverse_lazy('usuario_lista')
        context['entidad'] = 'Usuarios'
        return context

# ===============================
# Vistas para Habitaciones (clases)
# ===============================
class HabitacionListView(ListView):
    model = Habitacion
    template_name = 'hotel/lista_habitaciones.html'
    context_object_name = 'habitaciones'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Habitaciones'
        context['crear_url'] = reverse_lazy('habitacion_crear')
        context['entidad'] = 'Habitaciones'
        return context

class HabitacionCreateView(CreateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = 'hotel/form_habitacion.html'
    success_url = reverse_lazy('habitacion_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Nueva Habitación'
        context['listar_url'] = reverse_lazy('habitacion_lista')
        context['entidad'] = 'Habitaciones'
        return context

class HabitacionUpdateView(UpdateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = 'hotel/form_habitacion.html'
    success_url = reverse_lazy('habitacion_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Habitación'
        context['listar_url'] = reverse_lazy('habitacion_lista')
        context['entidad'] = 'Habitaciones'
        return context

class HabitacionDeleteView(DeleteView):
    model = Habitacion
    template_name = 'hotel/eliminar_habitacion.html'
    success_url = reverse_lazy('habitacion_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Habitación'
        context['listar_url'] = reverse_lazy('habitacion_lista')
        context['entidad'] = 'Habitaciones'
        return context

# ===============================
# Vistas para Capacitaciones (clases)
# ===============================
class CapacitacionListView(ListView):
    model = Capacitacion
    template_name = 'capacitaciones/lista_capacitaciones.html'
    context_object_name = 'capacitaciones'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Capacitaciones'
        context['crear_url'] = reverse_lazy('capacitacion_crear')
        context['entidad'] = 'Capacitaciones'
        context['campos'] = ['nombre', 'fecha_inicio', 'fecha_finalizacion', 'descripcion']
        return context

class CapacitacionCreateView(CreateView):
    model = Capacitacion
    form_class = CapacitacionForm
    template_name = 'capacitaciones/form_capacitacion.html'
    success_url = reverse_lazy('capacitacion_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Nueva Capacitación'
        context['listar_url'] = reverse_lazy('capacitacion_lista')
        context['entidad'] = 'Capacitaciones'
        return context

class CapacitacionUpdateView(UpdateView):
    model = Capacitacion
    form_class = CapacitacionForm
    template_name = 'capacitaciones/form_capacitacion.html'
    success_url = reverse_lazy('capacitacion_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Capacitación'
        context['listar_url'] = reverse_lazy('capacitacion_lista')
        context['entidad'] = 'Capacitaciones'
        return context

class CapacitacionDeleteView(DeleteView):
    model = Capacitacion
    template_name = 'capacitaciones/eliminar_capacitacion.html'
    success_url = reverse_lazy('capacitacion_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Capacitación'
        context['listar_url'] = reverse_lazy('capacitacion_lista')
        context['entidad'] = 'Capacitaciones'
        return context