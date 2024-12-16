import numpy as np
import tensorflow as tf
from .config import COLOR_CATEGORIES

def load_model():    
    # Carrega o modelo treinado a partir do arquivo especificado.
    # O modelo foi treinado e salvo com o nome 'color_model.h5' na pasta 'inference/model'.
    return tf.keras.models.load_model('inference/model/color_model.h5')

def predict_color(rgb_values):
    # Recebe um valor RGB e faz a predição da cor correspondente.
    # O modelo é carregado, a predição é realizada e a cor prevista é retornada.
    
    model = load_model()  # Carregar o modelo treinado
    prediction = model.predict(np.array([rgb_values]))  # Realizar a predição
    predicted_index = np.argmax(prediction)  # Obter o índice da cor com maior probabilidade
    return COLOR_CATEGORIES[predicted_index]  # Retorna o nome da cor com base no índice previsto

# Exemplo de uso:
if __name__ == '__main__':
    # Valores RGB para teste (exemplo: RGB para a cor roxa)
    rgb_values = [118,181,45]  # Valor RGB de teste
    color_name = predict_color(rgb_values)  # Prever o nome da cor
    print(f"Valor RGB: {rgb_values}")  # Exibe os valores RGB de entrada
    print(f"Cor prevista: {color_name}")  # Exibe o nome da cor prevista

# Executar python -m inference.predict
