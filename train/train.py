# Importações necessárias para construir, treinar e analisar o modelo
import tensorflow as tf  # Biblioteca para aprendizado profundo
from tensorflow.keras.models import Sequential  # Classe para criar modelos sequenciais
from tensorflow.keras.layers import Dense  # Camada densa (totalmente conectada)
from tensorflow.keras.optimizers import Adam  # Otimizador Adam
from .preprocess import load_data  # Função personalizada para carregar os dados
from .config import EPOCHS, BATCH_SIZE, LEARNING_RATE  # Configurações do treinamento
import os  # Biblioteca para manipulação de caminhos
import matplotlib.pyplot as plt  # Biblioteca para geração de gráficos
from datetime import datetime  # Biblioteca para trabalhar com data e hora

def create_model():
    """
    Define e compila o modelo de rede neural.

    O modelo é composto por:
    - Uma camada oculta com 10 neurônios e função de ativação 'sigmoid'.
    - Uma camada de saída com 9 neurônios (um para cada classe) e ativação 'softmax'.
    """
    model = Sequential([
        Dense(10, input_shape=(3,), activation='sigmoid'),  # Camada oculta
        Dense(9, activation='softmax')  # Camada de saída
    ])
    model.compile(
        loss='categorical_crossentropy',  # Função de perda para problemas de classificação
        optimizer=Adam(LEARNING_RATE),  # Otimizador Adam com taxa de aprendizado configurada
        metrics=['accuracy']  # Métrica para avaliar o desempenho do modelo
    )
    return model

def plot_training_history(history, timestamp):
    """
    Gera gráficos de perda (loss) e acurácia (accuracy) durante o treinamento.

    Args:
        history (History): Histórico do treinamento contendo perda e acurácia por época.
        timestamp (str): Timestamp para nomear o arquivo do gráfico.
    """
    # Recuperar os valores de perda e acurácia do histórico
    loss = history.history['loss']  # Perda por época
    accuracy = history.history.get('accuracy', [])  # Acurácia por época (se disponível)
    epochs = range(1, len(loss) + 1)  # Número de épocas

    # Criar o gráfico da perda
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(epochs, loss, 'b-o', label='Perda (loss)')
    plt.title('Evolução da Perda')
    plt.xlabel('Épocas')
    plt.ylabel('Perda')
    plt.legend()

    # Criar o gráfico da acurácia (se disponível)
    if accuracy:
        plt.subplot(1, 2, 2)
        plt.plot(epochs, accuracy, 'g-o', label='Acurácia')
        plt.title('Evolução da Acurácia')
        plt.xlabel('Épocas')
        plt.ylabel('Acurácia')
        plt.legend()

    # Ajustar o layout para melhor visualização
    plt.tight_layout()

    # Salvar os gráficos em um arquivo com o timestamp no nome
    plt.savefig(
        os.path.join(
            os.path.dirname(__file__),
            'loss_accuracy_plot_results',
            f'{timestamp}_{EPOCHS}_loss_accuracy_plot.png'
        )
    )
    plt.show()  # Exibir os gráficos

def train_model():
    """
    Carrega os dados de entrada e saída, treina o modelo e gera gráficos de análise.

    Etapas:
    - Carregar dados de treinamento.
    - Criar o modelo.
    - Treinar o modelo com base nos dados carregados.
    - Salvar o modelo treinado com timestamp e número de épocas no nome do arquivo.
    - Gerar gráficos para análise de perda e acurácia.
    """
    # Caminho para o arquivo de dados
    filepath = os.path.join(os.path.dirname(__file__), 'data', 'colors.json')

    # Carregar os dados de entrada (features) e saída (labels)
    inputs , outputs = load_data(filepath)

    # Criar o modelo de rede neural
    model = create_model()

    # Treinar o modelo e capturar o histórico de métricas
    history = model.fit(inputs, outputs, epochs=EPOCHS, batch_size=BATCH_SIZE)

    # Obter a data e hora atual no formato 'YYYYMMDD_HHMM' para uso no nome do arquivo
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')

    # Gerar o caminho completo para o arquivo do modelo com o timestamp
    model_filepath = os.path.join(
        os.path.dirname(__file__),
        'model',
        f'{timestamp}_{EPOCHS}_color_model.h5'
    )

    # Salvar o modelo treinado
    model.save(model_filepath)

    # Gerar gráficos de perda e acurácia durante o treinamento
    plot_training_history(history, timestamp)

# Bloco principal: executa o treinamento se o script for executado diretamente
if __name__ == '__main__':
    train_model()

# Observação:
# Para executar este script, use o comando:
# python -m inference.predict