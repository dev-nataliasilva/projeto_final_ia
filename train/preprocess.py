# Importações necessárias
import json  # Para manipulação de arquivos JSON
import numpy as np  # Biblioteca para operações numéricas
from tensorflow.keras.utils import to_categorical  # Para converter classes em formato one-hot
from .config import COLOR_CATEGORIES  # Lista de categorias de cores definida na configuração

def load_data(filepath):
    """
    Carrega os dados de cores do arquivo JSON e os processa para treinamento.

    Args:
        filepath (str): Caminho para o arquivo JSON contendo os dados das cores.

    Returns:
        tuple: Dois arrays numpy:
            - entradas: Matriz com as cores RGB (features).
            - respostas: Vetores one-hot correspondentes às categorias das cores (labels).
    """
    # Abrir o arquivo JSON contendo os dados das cores
    with open(filepath, 'r') as file:
        colors = json.load(file)  # Carregar o conteúdo do arquivo como uma lista de dicionários

    # Listas para armazenar os dados de entrada (cores RGB) e saída (categorias)
    inputs, outputs = [], []

    # Iterar sobre cada categoria de cor no JSON
    for index, color in enumerate(colors):
        # Converter o índice da cor para o formato one-hot
        codigo_cor = to_categorical(index, num_classes=len(COLOR_CATEGORIES))

        # Iterar sobre os valores RGB associados a essa cor
        for rgb_value in color["valores"]:
            inputs.append(rgb_value)  # Adicionar o valor RGB à lista de entradas
            outputs.append(codigo_cor)  # Adicionar o código one-hot à lista de respostas

    # Converter as listas de entradas e respostas para arrays numpy
    inputs = np.array(inputs) / 255.0   # Array de cores RGB
    outputs = np.array(outputs)  # Array de categorias one-hot

    # Retornar as entradas e respostas processadas
    return inputs, outputs
