import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# CLAVE DE SEGURIDAD (En producción real es recomendable usar variables de entorno)
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-tu-clave-secreta-aqui')

# Modo Depuración: False en producción
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Dominio / Hosts permitidos
ALLOWED_HOSTS = ['*']  # Permite cualquier dominio o IP asignada por el proveedor de hosting


# APPS INSTALADAS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Tu aplicación
    'votaciones',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Sirve archivos estáticos (imágenes, CSS) en producción
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'festival_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'festival_project.wsgi.application'


# BASE DE DATOS
# En desarrollo local usas MySQL. Para despliegue rápido, si el servidor no te da MySQL de inmediato,
# puedes usar SQLite como fallback o configurar las credenciales de tu MySQL remoto.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'festival_vallenato',
        'USER': 'root',
        'PASSWORD': '',  # Tu contraseña local de MySQL
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# VALIDACIÓN DE CONTRASEÑAS
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# IDIOMA Y ZONA HORARIA
LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# ARCHIVOS ESTÁTICOS (CSS, JavaScript, Imágenes)
STATIC_URL = '/static/'

# Carpeta de donde Django recopilará todos los estáticos para el servidor
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Almacenamiento con compresión y caché para producción mediante WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# CLAVE PRIMARIA DEFAULT
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# REDIRECCIONES DE AUTENTICACIÓN
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'