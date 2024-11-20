# inference/utils.py

def preprocess_input(rgb):
    """Normaliza a entrada RGB, se necessário."""
    return rgb / 255.0  # Normaliza os valores para o intervalo [0, 1]
