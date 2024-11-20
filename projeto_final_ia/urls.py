from django.urls import path
from .views import color_prediction  # Importa a view de previsão de cor

urlpatterns = [
    path('api/predict-color/', color_prediction, name='color_prediction'),
]
