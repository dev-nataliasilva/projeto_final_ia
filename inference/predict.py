# inference/predict.py
import numpy as np
import tensorflow as tf
from inference.config import COLOR_CATEGORIES

def load_model():
    return tf.keras.models.load_model('inference/model/color_model.h5')

def predict_color(rgb_values):
    model = load_model()
    prediction = model.predict(np.array([rgb_values]))
    predicted_index = np.argmax(prediction)
    return COLOR_CATEGORIES[predicted_index]

# Exemplo de uso:
if __name__ == '__main__':
    rgb_values = [255, 0, 0]  # Valor RGB de teste
    color_name = predict_color(rgb_values)
    print(f"Cor prevista: {color_name}")
