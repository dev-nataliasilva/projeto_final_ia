# Número de épocas para o treinamento. Define quantas vezes o modelo irá
# passar por todos os dados de treinamento.
EPOCHS = 150

# Tamanho do batch (lote) durante o treinamento. Define o número de amostras
# que o modelo processa antes de atualizar os pesos.
BATCH_SIZE = 16

# Taxa de aprendizado usada pelo otimizador durante o treinamento. Determina
# o tamanho dos passos dados ao ajustar os pesos do modelo.
LEARNING_RATE = 0.001

# Lista de categorias de cores. Cada cor na lista corresponde a uma classe
# que será usada para treinar o modelo a identificar cores com base em seu código RGB.
COLOR_CATEGORIES = [
    'Branco', 'Preto', 'Azul', 'Vermelho', 'Verde', 'Laranja', 'Amarelo', 'Roxo', 'Marrom'
]
