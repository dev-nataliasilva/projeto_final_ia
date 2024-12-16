import json  # Para trabalhar com arquivos JSON
import random  # Para gerar números aleatórios


def generate_variations(base_colors, num_variations=10, variation_range=10):
    """
    Gera variações de cores ajustando aleatoriamente os valores RGB.

    Args:
        base_colors (list): Lista de cores base no formato [R, G, B].
        num_variations (int): Número de variações para gerar.
        variation_range (int): Variação máxima em cada componente RGB (+/-).

    Returns:
        list: Lista de cores geradas, incluindo as originais.
    """
    extended_colors = []  # Lista para armazenar as cores expandidas

    while len(extended_colors) < num_variations:
        for color in base_colors:
            if len(extended_colors) >= num_variations:
                break
            # Adiciona a cor original
            extended_colors.append(color)
            # Gera uma variação da cor
            variation = [
                max(0, min(255, color[0] + random.randint(-variation_range, variation_range))),  # R
                max(0, min(255, color[1] + random.randint(-variation_range, variation_range))),  # G
                max(0, min(255, color[2] + random.randint(-variation_range, variation_range))),  # B
            ]
            extended_colors.append(variation)  # Adiciona a variação à lista de cores expandidas

    return extended_colors[:num_variations]  # Garante que o tamanho final seja o desejado


def expand_and_balance_colors(input_filepath, output_filepath, target_size=100, variation_range=10):
    """
    Expande e balanceia a base de dados de cores, gerando variações e formatando a saída.

    Args:
        input_filepath (str): Caminho para o arquivo colors.json original.
        output_filepath (str): Caminho para salvar o novo arquivo colors_expandido.json.
        target_size (int): Número de valores por categoria após balanceamento.
        variation_range (int): Variação máxima em cada componente RGB (+/-).
    """
    # Abre e lê o arquivo JSON com os dados de cores
    with open(input_filepath, 'r') as file:
        color_data = json.load(file)

    balanced_data = []  # Lista para armazenar os dados balanceados

    for color in color_data:
        nome = color["nome"]
        valores = color["valores"]

        # Se os valores já são suficientes, corta até o target_size
        if len(valores) >= target_size:
            valores_balanceados = random.sample(valores, target_size)
        else:
            # Gera variações passando repetidamente por todas as cores originais
            valores_balanceados = generate_variations(
                valores,
                num_variations=target_size,
                variation_range=variation_range
            )

        # Adiciona os dados formatados no formato correto
        balanced_data.append({
            "nome": nome,
            "valores": valores_balanceados
        })

    # Salva os dados balanceados e formatados em um novo arquivo JSON
    with open(output_filepath, 'w') as file:
        json.dump(balanced_data, file, indent=2, ensure_ascii=False)

    print(f"Dados salvos em: {output_filepath}")


# Caminhos para os arquivos de entrada e saída
input_file = 'train/data/colors.json'  # Arquivo de entrada com as cores originais
output_file = 'train/data/colors_expandido.json'  # Arquivo de saída para as cores balanceadas e expandidas

# Gera a base de dados expandida e balanceada
expand_and_balance_colors(input_file, output_file, target_size=500, variation_range=10)

if __name__ == '__main__':
    print("Base de dados sendo balanceada e formatada...")