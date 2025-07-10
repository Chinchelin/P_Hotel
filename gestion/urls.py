from django.urls import path
from . import views
from .views import (
    UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView,
    HabitacionListView, HabitacionCreateView, HabitacionUpdateView, HabitacionDeleteView,
    CapacitacionListView, CapacitacionCreateView, CapacitacionUpdateView, CapacitacionDeleteView
)

urlpatterns = [
    # Páginas básicas
    path('', views.pagina, name='pagina'),
    path('login/', views.login, name='login'),
    path('panel/', views.panel_control, name='panel_control'),
    
    # URLs para Usuarios
    path('usuarios/', UsuarioListView.as_view(), name='usuario_lista'),
    path('usuarios/crear/', UsuarioCreateView.as_view(), name='usuario_crear'),
    path('usuarios/editar/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario_editar'),
    path('usuarios/eliminar/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario_eliminar'),
    
    # URLs para Habitaciones
    path('habitaciones/', HabitacionListView.as_view(), name='habitacion_lista'),
    path('habitaciones/crear/', HabitacionCreateView.as_view(), name='habitacion_crear'),
    path('habitaciones/editar/<int:pk>/', HabitacionUpdateView.as_view(), name='habitacion_editar'),
    path('habitaciones/eliminar/<int:pk>/', HabitacionDeleteView.as_view(), name='habitacion_eliminar'),
    
    # URLs para Capacitaciones
    path('capacitaciones/', CapacitacionListView.as_view(), name='capacitacion_lista'),
    path('capacitaciones/crear/', CapacitacionCreateView.as_view(), name='capacitacion_crear'),
    path('capacitaciones/editar/<int:pk>/', CapacitacionUpdateView.as_view(), name='capacitacion_editar'),
    path('capacitaciones/eliminar/<int:pk>/', CapacitacionDeleteView.as_view(), name='capacitacion_eliminar'),
    
    # Otras URLs existentes...
    path('clientes/tabla/', views.tabla_clientes, name='tabla_clientes'),
    path('reservas/', views.reservas, name='reservas'),
    
]