"""
Django settings for projeto_final_ia project.
"""

import sys
from pathlib import Path
import os

# Caminho para o diretório do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Adiciona a pasta inference ao Python path
sys.path.append(str(BASE_DIR / "inference"))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configurações básicas
SECRET_KEY = 'django-insecure-o)t8bpups7nbzsfnh#jw+b=px$a1iq0rtp7!cnr1yv*+%8!bie'
DEBUG = False
ALLOWED_HOSTS = [
    'ondesalvei-afacdb17af64.herokuapp.com',  # Adicione este domínio
    #'localhost',  # Para desenvolvimento local
    #'127.0.0.1',  # Para desenvolvimento local
]

# Aplicativos instalados - apenas o necessário para uma API
INSTALLED_APPS = [    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
    'django.middleware.common.CommonMiddleware',
]


# Configuração de URL e WSGI
ROOT_URLCONF = 'projeto_final_ia.urls'
WSGI_APPLICATION = 'projeto_final_ia.wsgi.application'

# Banco de dados - SQLite para desenvolvimento rápido
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}

# Internacionalização
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos - pode ser ajustado para deploy
STATIC_URL = 'static/'

# Tipo de campo padrão para chaves primárias
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuração para Django REST Framework (DRF)
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}
