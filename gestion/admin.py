from django.contrib import admin
from .models import (
    Usuario, Cliente, Habitacion, Reserva, DetalleReserva,
    CheckIn, CheckOut, Categoria, Marca, Producto,
    Proveedor, Compra, DetalleCompra, Venta, DetalleVenta,
    Factura, Tarea, AsignacionTarea, Capacitacion,
    AsistenciaCapacitacion, ReporteOcupacion
)

# Registrar todos los modelos en el panel de administración
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Habitacion)
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
admin.site.register(Capacitacion)
admin.site.register(AsistenciaCapacitacion)
admin.site.register(ReporteOcupacion)
