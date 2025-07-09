from django.urls import path
from . import views
from gestion.views import tabla_clientes
from gestion.views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from gestion.views import ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView

urlpatterns = [


path('tabla/', ClienteListView.as_view(), name='tabla_clientes'),

# Rutas CRUD para clientes
# path('clientes/crear/', cliente_create, name='cliente_create')
path('clientes/crear/', ClienteCreateView.as_view(), name='cliente_crear'),
# path('clientes/<int:id>/editar/', cliente_update, name='cliente_update')
path('clientes/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_editar'),
#clientes para eliminar
path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_eliminar'),


# etc.







    # Página principal y login
    path('', views.pagina, name='pagina'),
    path('login/', views.login, name='login'),

    # Panel de control
    path('panelcontrol/', views.panel_control, name='panelcontrol'),

    # Usuarios
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/asignaciones/', views.asignaciones, name='asignaciones'),

    # Clientes
    path('clientes/', ClienteListView.as_view(), name='clientes'),

    # Hotel
    path('hotel/habitaciones/', views.habitaciones, name='habitaciones'),
    path('hotel/reservas/', views.reservas, name='reservas'),
    path('hotel/reservas/detalle/', views.detalle_reservas, name='detalle_reservas'),
    path('hotel/checkins/', views.checkins, name='checkins'),
    path('hotel/checkouts/', views.checkouts, name='checkouts'),

    # Inventario
    path('inventario/productos/', views.productos, name='productos'),
    path('inventario/categorias/', views.categorias, name='categorias'),
    path('inventario/marcas/', views.marcas, name='marcas'),

    # Compras
    path('proveedores/', ProveedorListView.as_view(), name='tabla_proveedores'),
    path('proveedores/crear/', ProveedorCreateView.as_view(), name='proveedor_crear'),
    path('proveedores/editar/<int:pk>/', ProveedorUpdateView.as_view(), name='proveedor_editar'),
    path('proveedores/eliminar/<int:pk>/', ProveedorDeleteView.as_view(), name='proveedor_eliminar'),
    path('compras/', views.compras, name='compras'),
    path('compras/detalle/', views.detalle_compras, name='detalle_compras'),

    # Ventas
    path('ventas/', views.ventas, name='ventas'),
    path('ventas/detalle/', views.detalle_ventas, name='detalle_ventas'),
    path('ventas/facturas/', views.facturas, name='facturas'),

    # Tareas y Capacitaciones
    path('gestion/tareas/', views.tareas, name='tareas'),
    path('gestion/capacitaciones/', views.capacitaciones, name='capacitaciones'),
    path('gestion/asistencias/', views.asistencias, name='asistencias'),

    # Reportes
    path('reportes/', views.reportes, name='reportes'),
]
