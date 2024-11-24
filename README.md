## Módulo de Inteligência Artificial - projeto _Onde Salvei_?
Reconhecimento de Cores com Redes Neurais Redes Neurais Artificiais (RNA) implementadas com o framework TensorFlow/Keras para treinar um modelo capaz de classificar cores com base em valores RGB. A aplicação possui uma estrutura modular, permitindo o treinamento, inferência e expansão de dados de forma simples e eficiente.

### 📋 Estrutura do Projeto
O projeto está dividido em três componentes principais:
- train/: Contém scripts relacionados ao treinamento do modelo.
    - train.py: Script principal para treinar o modelo.
    - data/: Contém os arquivos JSON de cores, incluindo os dados originais e os expandidos.
    - model/: Diretório onde o modelo treinado será salvo.
    - config.py: Arquivo de configuração para definir parâmetros do treinamento, como número de épocas, tamanho do batch, taxa de aprendizado, categoria de cores que serão reconhecidas, etc.
- inference/: Será utilizado para realizar inferências no modelo treinado (Reconhecimento de cores).
    - predict.py: Script que executa o reconhecimento de cor de acordo com o RGB inserido.
    - config.py: Arquivo de configuração para definir parâmetros da categoria de cores que serão reconhecidas.
- projeto_final_ia/: Contém scripts relacionados a API.

### ⚙️ Funcionalidades
#### 1. Treinamento
O treinamento do modelo é realizado no script train/train.py, que:
- Carrega os dados de cores do arquivo colors.json.
- Define a estrutura da RNA com duas camadas densas:
    - Camada oculta com ativação sigmoid.
    - Camada de saída com ativação softmax.
- Treina o modelo com base nos parâmetros configurados em config.py.
- Gera gráficos de perda e acurácia ao longo das épocas para análise.
- Salva o modelo treinado com o nome no formatado.

#### 2. Base de Dados
O projeto utiliza um arquivo JSON (colors.json) com cores categorizadas e cada cor possui um conjunto de valores RGB associados.
- Expansão da Base de Dados:
    - O script gera variações dos valores RGB para enriquecer os dados de treinamento.
    - O arquivo resultante é salvo como colors_expandido.json.

#### 3. Inferência
Permite classificar novas cores fornecendo valores RGB e retornando a categoria correspondente.

#### 4. API
O projeto contém um endpoint POST que permite receber a requisição para reconhecer a cor RGB recebida.

### 🚀 Como Executar
- Requisitos:
    - Python 3.8+
- Pacotes listados no arquivo requirements.txt. Para instalá-los, renomeie o arquivo "requirements - Develop.txt" para "requirements.txt" e execute:
```bash
pip install -r requirements.txt
```

#### 1. Base de Dados (opcional)
- Por padrão, existe uma base de dados nomeada colors.json, entretanto, é possível expandir essa base para obter resultados mais precisos. Para executar o script expand_colors.py:
```bash
python train/expand_colors.py
```

#### 2. Treinamento
- Execute o treinamento do modelo com o comando:
```bash
python -m train.train
```
O treinamento irá gerar dois arquivos: o modelo treinado será salvo em train/model/ e os gráficos de perda e acurácia que serão salvos em train/loss_accuracy_plot_results/ para a análise de resultados. Os gráficos permitem visualizar como o modelo se comporta ao longo das épocas, ajudando a identificar possíveis overfitting ou underfitting.

#### 3. Predição
- Copie o modelo treinado que foi gerado ao executar o treinamento (localizado em train/model) e cole na pasta de model do módulo de inferência (localizado em inference/model).
- Renomeie o modelo treinado para "color_model.h5"
- Para testar, vá até o script predict.py e modifique o valor da variável "rgb_values" para um valor RGB qualquer.
- Execute o script de predição usando o comando:
```bash
python -m inference.predict
```
- O resultado será exibido no console.

#### 3. API (Opcional)
Caso deseje usar a função para reconhecer cores como um endpoint, existe um endpoint POST pronto para ser utilizado. Para iniciar a API, basta executar o comando:
```python
python manage.py runserver 
```

### 🔧 Configurações
O arquivo config.py permite personalizar os seguintes parâmetros:
- EPOCHS: Número de épocas para o treinamento.
- BATCH_SIZE: Quantidade de amostras por batch.
- LEARNING_RATE: Taxa de aprendizado do otimizador.
- COLOR_CATEGORIES: Lista de categorias de cores (usada para rotular as saídas do modelo). Pode-se criar quantas categorias de cores que desejar para serem identificadas. Entretanto, é essencial montar uma base de dados (train/colors.json) que contenham as novas cores e atualizar as informações da camada de inference conforme as mudança feitas.

### 🗂️ Exemplos de Dados
- Entrada: Exemplo de estrutura do arquivo colors.json (base de dados) presente na camada de treinamento:
```json
[
  {
    "nome": "Vermelho",
    "valores": [[255, 0, 0], [250, 50, 50], ...]
  },
  {
    "nome": "Verde",
    "valores": [[0, 255, 0], [50, 250, 50], ...]
  }
]
```
- Saída
Exemplo de classificação gerada na camada de inferência:
Entrada: [0, 128, 0]
Saída: "Verde"

### 📝 Licença
Este projeto está sob a licença MIT. Sinta-se livre para utilizá-lo e modificá-lo conforme necessário.

### 📝 Objetivo
Este código integra o ecossistema do produto _Onde Salvei?_, desenvolvido como parte do Projeto de Conclusão de Curso da graduação em Ciência da Computação.
