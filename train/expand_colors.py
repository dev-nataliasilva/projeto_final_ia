import json  # Para trabalhar com arquivos JSON
import random  # Para gerar números aleatórios

def generate_variations(base_colors, num_variations=10, variation_range=10):
    """
    Gera variações de cores ajustando aleatoriamente os valores RGB.
    
    Args:
        base_colors (list): Lista de cores base no formato [R, G, B].
        num_variations (int): Número de variações para gerar por cor base.
        variation_range (int): Variação máxima em cada componente RGB (+/-).
    
    Returns:
        list: Lista de cores geradas, incluindo as originais.
    """
    extended_colors = []  # Lista para armazenar as cores expandidas

    for color in base_colors:
        extended_colors.append(color)  # Adiciona a cor original à lista
        for _ in range(num_variations):
            # Gera uma variação aleatória para cada componente RGB da cor
            variation = [
                max(0, min(255, color[0] + random.randint(-variation_range, variation_range))),  # Variação do componente R
                max(0, min(255, color[1] + random.randint(-variation_range, variation_range))),  # Variação do componente G
                max(0, min(255, color[2] + random.randint(-variation_range, variation_range))),  # Variação do componente B
            ]
            extended_colors.append(variation)  # Adiciona a variação à lista de cores expandidas

    return extended_colors  # Retorna a lista de cores expandidas

def expand_color_data(input_filepath, output_filepath, num_variations=50, variation_range=10):
    """
    Expande a base de dados de cores gerando variações para cada cor existente.

    Args:
        input_filepath (str): Caminho para o arquivo colors.json original.
        output_filepath (str): Caminho para salvar o novo arquivo colors_expandido.json.
        num_variations (int): Número de variações para gerar por cor base.
        variation_range (int): Variação máxima em cada componente RGB (+/-).
    """
    # Abre e lê o arquivo JSON com os dados de cores
    with open(input_filepath, 'r') as file:
        color_data = json.load(file)

    expanded_data = []  # Lista para armazenar os dados expandidos

    # Para cada cor na base de dados, gerar variações
    for color in color_data:
        expanded_colors = generate_variations(color["valores"], num_variations, variation_range)
        expanded_data.append({
            "nome": color["nome"],  # Mantém o nome da cor
            "valores": expanded_colors  # Adiciona as cores expandidas
        })

    # Salva os dados expandidos em um novo arquivo JSON
    with open(output_filepath, 'w') as file:
        json.dump(expanded_data, file, indent=4)  # Salva com indentação para facilitar a leitura

# Caminhos para os arquivos de entrada e saída
input_file = 'train/data/colors.json'  # Arquivo de entrada com as cores originais
output_file = 'train/data/colors_expandido.json'  # Arquivo de saída para as cores expandidas

# Gera a base de dados expandida
expand_color_data(input_file, output_file)

if __name__ == '__main__':
    # Caminhos para os arquivos
    input_file = 'train/data/colors.json'
    output_file = 'train/data/colors_expandido.json'

    # Número de variações por cor e o alcance da variação
    num_variations = 50
    variation_range = 10

    print("Expandindo a base de dados...")  # Mensagem de status
    expand_color_data(input_file, output_file, num_variations, variation_range)  # Chama a função para expandir os dados
    print(f"Base expandida salva em {output_file}")  # Confirmação de que os dados foram salvos