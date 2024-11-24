from django.urls import path
from .views import color_prediction  # Importa a view de previsão de cor

urlpatterns = [
    # Define a rota para a previsão de cor. O caminho '/api/predict-color/' será associado à função color_prediction.
    # O nome 'color_prediction' é um identificador que pode ser utilizado para referenciar essa URL em outros lugares.
    path('api/predict-color/', color_prediction, name='color_prediction'),
]