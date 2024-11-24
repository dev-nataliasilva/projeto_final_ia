"""
Configuração WSGI para o projeto projeto_final_ia.

Este arquivo expõe a aplicação WSGI como uma variável de nível de módulo chamada ``application``.

Para mais informações sobre este arquivo, veja:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os  # Importa o módulo 'os' para interagir com o sistema operacional

from django.core.wsgi import get_wsgi_application  # Importa a função para obter a aplicação WSGI do Django

# Define a variável de ambiente 'DJANGO_SETTINGS_MODULE', que aponta para o arquivo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_final_ia.settings')

# Chama 'get_wsgi_application' para obter a aplicação WSGI do Django, que será usada pelo servidor
application = get_wsgi_application()