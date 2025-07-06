from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Todo el sistema gestionado desde la app "gestion"
    path('', include('gestion.urls')),
]
