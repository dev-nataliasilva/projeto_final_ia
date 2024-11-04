# train/preprocess.py
import json
import numpy as np
from tensorflow.keras.utils import to_categorical
from .config import COLOR_CATEGORIES

def load_data(filepath):
    with open(filepath, 'r') as file:
        cores = json.load(file)

    entradas, respostas = [], []
    for indice, cor in enumerate(cores):
        codigo_cor = to_categorical(indice, num_classes=len(COLOR_CATEGORIES))
        for cor_rgb in cor["valores"]:
            entradas.append(cor_rgb)
            respostas.append(codigo_cor)

    entradas = np.array(entradas)
    respostas = np.array(respostas)
    return entradas, respostas
