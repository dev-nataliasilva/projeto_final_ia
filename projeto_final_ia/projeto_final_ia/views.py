from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from inference.predict import predict_color  # Importa a função de previsão de cor

@api_view(['POST'])
def color_prediction(request):
    rgb_values = request.data.get('rgb')
    
    # Validação básica do input
    if rgb_values is None or len(rgb_values) != 3:
        return Response(
            {'error': 'Por favor, forneça um array RGB válido com três valores numéricos.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        # Chama a função de previsão de cor da IA
        color_name = predict_color(rgb_values)
        return Response({'predicted_color': color_name}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(
            {'error': f"Erro ao prever a cor: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
