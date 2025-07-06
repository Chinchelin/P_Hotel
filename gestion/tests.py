import os
import django

# 🧠 Asegura que se cargue la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HotelPlaza.settings')

# 🧠 Inicializa Django (requiere que esté bien configurado BASE_DIR y apps)
django.setup()

# ✅ Ahora puedes importar tus modelos
from gestion.models import Categoria

# ✅ Consultar y mostrar todas las categorías
categorias = Categoria.objects.all()

for categoria in categorias:
    print(f"{categoria.id} - {categoria.nombre} - {categoria.descripcion}")
