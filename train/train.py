# train/train.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from .preprocess import load_data
from .config import EPOCHS, BATCH_SIZE, LEARNING_RATE
import os
import matplotlib.pyplot as plt
from datetime import datetime

def create_model():
    """
    Define e compila o modelo de rede neural.
    """
    model = Sequential([
        Dense(10, input_shape=(3,), activation='sigmoid'),  # Camada oculta com 10 neurônios
        Dense(9, activation='softmax')  # Camada de saída com 9 neurônios
    ])
    model.compile(
        loss='categorical_crossentropy',  # Função de perda
        optimizer=Adam(LEARNING_RATE),  # Otimizador Adam
        metrics=['accuracy']  # Métrica de avaliação
    )
    return model

def plot_training_history(history):
    """
    Gera gráficos de perda e acurácia durante o treinamento.
    """
    # Recuperar dados do histórico
    loss = history.history['loss']  # Perda por época
    accuracy = history.history.get('accuracy', [])  # Acurácia por época, se disponível
    epochs = range(1, len(loss) + 1)

    # Gráfico da perda
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(epochs, loss, 'b-o', label='Perda (loss)')
    plt.title('Evolução da Perda')
    plt.xlabel('Épocas')
    plt.ylabel('Perda')
    plt.legend()

    # Gráfico da acurácia (se disponível)
    if accuracy:
        plt.subplot(1, 2, 2)
        plt.plot(epochs, accuracy, 'g-o', label='Acurácia')
        plt.title('Evolução da Acurácia')
        plt.xlabel('Épocas')
        plt.ylabel('Acurácia')
        plt.legend()

    # Ajustar layout e exibir os gráficos
    plt.tight_layout()

    # Salvar os gráficos em um arquivo com o número de épocas no nome
    plt.savefig(os.path.join(os.path.dirname(__file__), 'loss_accuracy_plot_results', f'loss_accuracy_plot_{EPOCHS}.png')); plt.show()
    plt.show()

def train_model():
    """
    Carrega os dados, treina o modelo e gera gráficos de análise.
    """
    # Caminho para o arquivo de dados
    filepath = os.path.join(os.path.dirname(__file__), 'data', 'colors.json')

    # Carregar dados de treinamento
    entradas, respostas = load_data(filepath)

    # Criar o modelo
    model = create_model()

    # Treinar o modelo e capturar o histórico
    history = model.fit(entradas, respostas, epochs=EPOCHS, batch_size=BATCH_SIZE)

   # Obter a data e hora atual no formato desejado
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')

    # Gerar o caminho completo para o arquivo com a data e hora no nome
    model_filepath = os.path.join(os.path.dirname(__file__), 'model', f'{timestamp}_color_model.h5')

    # Salvar o modelo treinado
    model.save(model_filepath)

    # Gerar gráficos de perda e acurácia
    plot_training_history(history)

if __name__ == '__main__':
    train_model()
