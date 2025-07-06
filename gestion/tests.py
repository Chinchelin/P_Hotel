import os
import django

# Establecer configuración del proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HotelPlaza.settings')
django.setup()

# Ahora puedes importar modelos
from gestion.models import Categoria

# Listar todas las categorías
categorias = Categoria.objects.all()

for categoria in categorias:
    print(f"{categoria.id} - {categoria.nombre} - {categoria.descripcion}")
