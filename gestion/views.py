from pyexpat.errors import messages
from django.shortcuts import render
from django.db.models import Q
from gestion.forms import BuscarCategoriaForm, BuscarMarcaForm, CategoriaForm
from .models import Categoria, Cliente
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Marca

# ==================================================================
# Categoria
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/listar.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        form = BuscarCategoriaForm(self.request.GET)
        
        if form.is_valid() and form.cleaned_data['nombre']:
            queryset = queryset.filter(
                Q(nombre__icontains=form.cleaned_data['nombre']) |
                Q(descripcion__icontains=form.cleaned_data['nombre'])
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_busqueda'] = BuscarCategoriaForm(self.request.GET or None)
        context['titulo'] = 'Listado de Categorías'
        context['crear_url'] = reverse_lazy('categoria_crear')
        return context

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/form.html'
    success_url = reverse_lazy('categoria_listar')
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoría creada exitosamente!')
        return super().form_valid(form)

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/form.html'
    success_url = reverse_lazy('categoria_listar')
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoría actualizada exitosamente!')
        return super().form_valid(form)

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/eliminar.html'
    success_url = reverse_lazy('categoria_listar')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Categoría eliminada exitosamente!')
        return super().delete(request, *args, **kwargs)
 # ==================================================================
 # ==================================================================
 # Marcas
class MarcaDetailView(DetailView):
    model = Marca
    template_name = 'marcas/detalle.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Detalle de Marca'
        context['listar_url'] = reverse_lazy('marcas_listar')
        return context
    
class MarcaListView(ListView):
    model = Marca
    template_name = 'marcas/listar.html'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = BuscarMarcaForm(self.request.GET)
        
        if form.is_valid() and form.cleaned_data['nombre']:
            nombre = form.cleaned_data['nombre']
            queryset = queryset.filter(
                Q(nombre__icontains=nombre) |
                Q(descripcion__icontains=nombre)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_busqueda'] = BuscarMarcaForm(self.request.GET or None)
        context['titulo'] = 'Listado de Marcas'
        context['crear_url'] = reverse_lazy('marcas_crear')
        context['entidad'] = 'Marcas'
        return context
    
class MarcaCreateView(CreateView):
    model = Marca
    fields = '__all__'
    template_name = 'marcas/form.html'
    success_url = reverse_lazy('marcas_listar')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creación de una Marca'
        context['entidad'] = 'Marcas'
        context['listar_url'] = reverse_lazy('marcas_listar')
        return context

class MarcaUpdateView(UpdateView):
    model = Marca
    fields = '__all__'
    template_name = 'marcas/form.html'
    success_url = reverse_lazy('marcas_listar')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edición de una Marca'
        context['entidad'] = 'Marcas'
        context['listar_url'] = reverse_lazy('marcas_listar')
        return context

class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'marcas/eliminar.html'
    success_url = reverse_lazy('marcas_listar')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminación de una Marca'
        context['entidad'] = 'Marcas'
        context['listar_url'] = reverse_lazy('marcas_listar')
        return context
# ===============================================================================
# ===============================================================================
# Clientes
def tabla_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/tabla_clientes.html', {'clientes': clientes})
# ===============================================================================

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
