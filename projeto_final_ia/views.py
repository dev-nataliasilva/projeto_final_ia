from rest_framework.decorators import api_view  # Importa o decorador 'api_view' para criar views de API
from rest_framework.response import Response  # Importa a classe 'Response' para enviar respostas HTTP
from rest_framework import status  # Importa o módulo 'status' para utilizar códigos de status HTTP
from inference.predict import predict_color  # Importa a função 'predict_color' que faz a previsão da cor

# Define a view para previsão de cor, que aceita requisições POST
@api_view(['POST'])
def color_prediction(request):
    # Obtém os valores RGB enviados no corpo da requisição
    rgb_values = request.data.get('rgb')
    
    # Validação básica para verificar se os valores RGB foram fornecidos corretamente
    # A validação garante que 'rgb' esteja presente e que tenha exatamente três valores
    if rgb_values is None or len(rgb_values) != 3:
        return Response(
            {'error': 'Por favor, forneça um array RGB válido com três valores numéricos.'},
            status=status.HTTP_400_BAD_REQUEST  # Retorna erro 400 (Bad Request) se a validação falhar
        )
    
    try:
        # Tenta prever a cor com base nos valores RGB fornecidos
        color_name = predict_color(rgb_values)
        
        # Retorna a cor prevista junto com o código de status 200 (OK)
        return Response({'predicted_color': color_name}, status=status.HTTP_200_OK)
    
    except Exception as e:
        # Em caso de erro, retorna uma mensagem de erro com o código de status 500 (Erro interno do servidor)
        return Response(
            {'error': f"Erro ao prever a cor: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )