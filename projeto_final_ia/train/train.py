# train/train.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from .preprocess import load_data
from .config import EPOCHS, BATCH_SIZE, LEARNING_RATE

def create_model():
    model = Sequential([
        Dense(10, input_shape=(3,), activation='sigmoid'),
        Dense(9, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', optimizer=Adam(LEARNING_RATE), metrics=['accuracy'])
    return model

def train_model():
    entradas, respostas = load_data('data/colors.json')
    model = create_model()
    model.fit(entradas, respostas, epochs=EPOCHS, batch_size=BATCH_SIZE)
    model.save('model/color_model.h5')

if __name__ == '__main__':
    train_model()
