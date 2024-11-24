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

# Configurações de arquivos estáticos
STATIC_URL = '/static/'  # URL para acessar arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Diretório onde os arquivos estáticos serão coletados

# Configurações básicas de segurança
SECRET_KEY = 'django-insecure-o)t8bpups7nbzsfnh#jw+b=px$a1iq0rtp7!cnr1yv*+%8!bie'  # Chave secreta para o Django
DEBUG = False  # Desativa o modo de debug em produção
ALLOWED_HOSTS = [
    'ondesalvei-ia-f31a49c64a2d.herokuapp.com',  # Endereço da aplicação IA no Heroku
    'https://ondesalvei-api-3e0bb38ffd71.herokuapp.com/,'  # Endereço da API no Heroku  
    'https://ondesalvei-afacdb17af64.herokuapp.com/',  # Host do frontend no Heroku
    #'localhost',  # Para desenvolvimento local
    #'127.0.0.1',  # Para desenvolvimento local
]

# Aplicativos instalados - apenas os necessários para uma API
INSTALLED_APPS = [    
    'django.contrib.auth',  # Sistema de autenticação do Django
    'django.contrib.contenttypes',  # Tipos de conteúdo do Django
    'django.contrib.sessions',  # Gerenciamento de sessões
    'django.contrib.messages',  # Mensagens do Django
    'django.contrib.staticfiles',  # Gerenciamento de arquivos estáticos
    'rest_framework',  # Django Rest Framework (DRF) para APIs REST
]

# Middleware - configurações para segurança e otimização
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Middleware para segurança
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Middleware para servir arquivos estáticos comprimidos
    'django.middleware.common.CommonMiddleware',  # Middleware comum
]

# Configuração de URL e WSGI
ROOT_URLCONF = 'projeto_final_ia.urls'  # Arquivo de URLs da aplicação
WSGI_APPLICATION = 'projeto_final_ia.wsgi.application'  # Aplicação WSGI para deploy

# Banco de dados - SQLite para desenvolvimento rápido
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',  # Banco de dados SQLite
    #     'NAME': BASE_DIR / 'db.sqlite3',  # Caminho para o banco de dados
    # }
}

# Internacionalização - configurações de idioma e fuso horário
LANGUAGE_CODE = 'en-us'  # Código do idioma
TIME_ZONE = 'UTC'  # Fuso horário
USE_I18N = True  # Habilita a internacionalização
USE_TZ = True  # Habilita o uso de fusos horários

# Arquivos estáticos - URL para arquivos estáticos
STATIC_URL = 'static/'

# Tipo de campo padrão para chaves primárias no banco de dados
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuração para Django REST Framework (DRF)
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # Renderiza a resposta como JSON
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',  # Interpreta as requisições como JSON
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [],  # Sem autenticação por padrão
    'DEFAULT_PERMISSION_CLASSES': [],  # Sem permissões por padrão
}

# Servindo arquivos estáticos de forma simplificada
# Configuração para usar o WhiteNoise, que serve arquivos estáticos diretamente no ambiente de produção
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'