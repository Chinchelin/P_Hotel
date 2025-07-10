from pathlib import Path
import os

# BASE_DIR apunta a la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent


# =====================
# Seguridad y entorno
# =====================

SECRET_KEY = 'django-insecure-1ae78!*kq$7!+hmto04fff)i@pnol6g&q5_^f^)5h%lcf93v1#'

DEBUG = True

ALLOWED_HOSTS = []  # Para producción, agrega tu dominio o ['*'] temporalmente para pruebas


# =====================
# Aplicaciones instaladas
# =====================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'widget_tweaks',  # Para mejor personalización de formularios
    
    # Local apps
    'gestion',  # App principal
]


# =====================
# Middleware
# =====================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =====================
# URLs y WSGI
# =====================

ROOT_URLCONF = 'HotelPlaza.urls'
WSGI_APPLICATION = 'HotelPlaza.wsgi.application'


# =====================
# Plantillas (Templates)
# =====================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'gestion', 'templates'),  # Carpeta principal de templates
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # Context processors personalizados (si los tienes)
                # 'gestion.context_processors.configuracion_general',
            ],
            'builtins': [
                'widget_tweaks.templatetags.widget_tweaks',  # Para usar widget_tweaks en templates
            ],
        },
    },
]


# =====================
# Base de datos (SQLite3)
# =====================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =====================
# Validación de contraseñas
# =====================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,  # Longitud mínima de contraseña
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# =====================
# Internacionalización
# =====================

LANGUAGE_CODE = 'es-co'        # Español de Colombia
TIME_ZONE = 'America/Bogota'   # Zona horaria colombiana

USE_I18N = True
USE_L10N = True
USE_TZ = True


# =====================
# Archivos estáticos (CSS, JS, imágenes)
# =====================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'gestion', 'static'),
]

# Configuración para producción (opcional)
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# =====================
# Configuración de autenticación
# =====================

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/panel/'
LOGOUT_REDIRECT_URL = '/'


# =====================
# Configuración de sesión
# =====================

SESSION_COOKIE_AGE = 86400  # 1 día en segundos
SESSION_SAVE_EVERY_REQUEST = True


# =====================
# Configuración extra
# =====================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración para emails (opcional, necesario para recuperación de contraseñas)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Solo para desarrollo
# EMAIL_HOST = 'smtp.tudominio.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'tu@email.com'
# EMAIL_HOST_PASSWORD = 'tupassword'

# Configuración de DataTables (opcional)
DATA_TABLES_DEFAULT_CONFIG = {
    'responsive': True,
    'language': {
        'url': '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json'
    }
}