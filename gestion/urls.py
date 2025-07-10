from django.urls import path
from . import views
from gestion.views import CategoriaCreateView, CategoriaDeleteView, CategoriaListView, CategoriaUpdateView, MarcaCreateView, MarcaDeleteView, MarcaDetailView, MarcaListView, MarcaUpdateView, tabla_clientes

urlpatterns = [

    #-----------------------------------------------------------------------------------
    # Marcas
    path('marcas/ver/<int:pk>/', MarcaDetailView.as_view(), name='marcas_ver'),
    path('marcas/marcas/', MarcaListView.as_view(), name='marcas_listar'),
    path('marcas/crear/', MarcaCreateView.as_view(), name='marcas_crear'),
    path('marcas/editar/<int:pk>/', MarcaUpdateView.as_view(), name='marcas_editar'),
    path('marcas/eliminar/<int:pk>/', MarcaDeleteView.as_view(), name='marcas_eliminar'),
    #------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------
    # Categorias
    path('categoria/', CategoriaListView.as_view(), name='categoria_listar'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name='categoria_crear'),
    path('categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_editar'),
    path('categoria/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_eliminar'),
    #------------------------------------------------------------------------------------
    
    
    
    
    
path('tabla/', tabla_clientes, name='tabla_clientes'),
# Rutas CRUD para clientes
# path('clientes/crear/', cliente_create, name='cliente_create')
# path('clientes/<int:id>/editar/', cliente_update, name='cliente_update')
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
    path('clientes/', views.clientes, name='clientes'),

    # Hotel
    path('hotel/habitaciones/', views.habitaciones, name='habitaciones'),
    path('hotel/reservas/', views.reservas, name='reservas'),
    path('hotel/reservas/detalle/', views.detalle_reservas, name='detalle_reservas'),
    path('hotel/checkins/', views.checkins, name='checkins'),
    path('hotel/checkouts/', views.checkouts, name='checkouts'),

    # Inventario
    path('inventario/productos/', views.productos, name='productos'),
    
    
   
    # Compras
    path('compras/proveedores/', views.proveedores, name='proveedores'),
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
