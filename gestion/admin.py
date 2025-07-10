from django.contrib import admin
from .models import (
    Usuario, Cliente, Habitacion, Reserva, DetalleReserva,
    CheckIn, CheckOut, Categoria, Marca, Producto,
    Proveedor, Compra, DetalleCompra, Venta, DetalleVenta,
    Factura, Tarea, AsignacionTarea, Capacitacion,
    AsistenciaCapacitacion, ReporteOcupacion
)
from .forms import UsuarioForm, HabitacionForm, CapacitacionForm

# Primero registra los modelos que quieres personalizar
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    form = UsuarioForm
    list_display = ('nombre', 'apellido', 'numero_documento', 'rol', 'estado')
    list_filter = ('rol', 'estado')
    search_fields = ('nombre', 'apellido', 'numero_documento')

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    form = HabitacionForm
    list_display = ('numero_habitacion', 'tipo_habitacion', 'capacidad', 'precio_noche', 'estado')
    list_filter = ('tipo_habitacion', 'estado')
    search_fields = ('numero_habitacion', 'descripcion')

@admin.register(Capacitacion)
class CapacitacionAdmin(admin.ModelAdmin):
    form = CapacitacionForm
    list_display = ('nombre', 'fecha_inicio', 'fecha_finalizacion')
    list_filter = ('fecha_inicio',)
    search_fields = ('nombre', 'descripcion')

# Luego registra el resto de modelos sin personalización
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(DetalleReserva)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Compra)
admin.site.register(DetalleCompra)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Factura)
admin.site.register(Tarea)
admin.site.register(AsignacionTarea)
admin.site.register(AsistenciaCapacitacion)
admin.site.register(ReporteOcupacion)