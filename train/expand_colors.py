import json
import random

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
    extended_colors = []

    for color in base_colors:
        extended_colors.append(color)  # Adiciona a cor original
        for _ in range(num_variations):
            variation = [
                max(0, min(255, color[0] + random.randint(-variation_range, variation_range))),
                max(0, min(255, color[1] + random.randint(-variation_range, variation_range))),
                max(0, min(255, color[2] + random.randint(-variation_range, variation_range))),
            ]
            extended_colors.append(variation)

    return extended_colors

def expand_color_data(input_filepath, output_filepath, num_variations=50, variation_range=10):
    """
    Expande a base de dados de cores gerando variações para cada cor existente.

    Args:
        input_filepath (str): Caminho para o arquivo colors.json original.
        output_filepath (str): Caminho para salvar o novo arquivo colors_expandido.json.
        num_variations (int): Número de variações para gerar por cor base.
        variation_range (int): Variação máxima em cada componente RGB (+/-).
    """
    with open(input_filepath, 'r') as file:
        color_data = json.load(file)

    expanded_data = []
    for color in color_data:
        expanded_colors = generate_variations(color["valores"], num_variations, variation_range)
        expanded_data.append({
            "nome": color["nome"],
            "valores": expanded_colors
        })

    with open(output_filepath, 'w') as file:
        json.dump(expanded_data, file, indent=4)

# Caminhos para os arquivos
input_file = 'train/data/colors.json'
output_file = 'train/data/colors_expandido.json'



# Gera a base expandida
expand_color_data(input_file, output_file)

if __name__ == '__main__':
    # Caminhos para os arquivos
    input_file = 'train/data/colors.json'
    output_file = 'train/data/colors_expandido.json'

    # Número de variações por cor e alcance de variação
    num_variations = 50
    variation_range = 10

    print("Expandindo a base de dados...")
    expand_color_data(input_file, output_file, num_variations, variation_range)
    print(f"Base expandida salva em {output_file}")
