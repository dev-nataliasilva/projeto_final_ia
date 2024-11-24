#!/usr/bin/env python
"""
Script utilitário para tarefas administrativas do Django.
Este script é usado para executar comandos do Django, como inicializar o servidor de desenvolvimento ou migrar bancos de dados.
"""

import os  # Biblioteca para interagir com o sistema operacional
import sys  # Biblioteca para manipular argumentos e o ambiente do Python

def main():
    """
    Função principal para executar tarefas administrativas.
    Define a configuração padrão do Django e executa os comandos passados via linha de comando.
    """
    # Define a variável de ambiente padrão para o módulo de configurações do Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_final_ia.settings')

    try:
        # Importa o método para executar comandos do Django a partir da linha de comando
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Exceção gerada caso o Django não esteja instalado ou configurado corretamente
        raise ImportError(
            "Não foi possível importar o Django. Verifique se ele está instalado "
            "e disponível na variável de ambiente PYTHONPATH. "
            "Você se lembrou de ativar o ambiente virtual?"
        ) from exc

    # Executa o comando passado como argumento na linha de comando
    execute_from_command_line(sys.argv)

# Este bloco verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == '__main__':
    # Chama a função principal
    main()

# Observação: Para iniciar o servidor de desenvolvimento, execute:
# python manage.py runserver