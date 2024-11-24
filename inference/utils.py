def preprocess_input(rgb):
    """Normaliza a entrada RGB, se necessário."""
    # A função recebe os valores RGB e os normaliza para o intervalo [0, 1].
    # Normalizar os valores de entrada é uma prática comum em modelos de aprendizado de máquina
    # para melhorar a estabilidade e a performance do treinamento e da inferência.
    # No caso, o valor máximo para cada componente de cor (R, G, B) é 255, 
    # então cada componente é dividido por 255 para que o valor final esteja no intervalo [0, 1].
    
    return rgb / 255.0  # Normaliza os valores para o intervalo [0, 1]