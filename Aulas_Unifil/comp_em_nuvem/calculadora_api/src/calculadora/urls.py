from rest_framework.urls import path
from calculadora.views import Adicao, Subtracao, Multiplicacao, Divisao

urlpatterns = [
    path('adicao/<int:a>/<int:b>/', Adicao.as_view()),
    path('subtracao/<int:a>/<int:b>/', Subtracao.as_view()),
    path('multiplicacao/<int:a>/<int:b>/', Multiplicacao.as_view()),
    path('divisao/<int:a>/<int:b>/', Divisao.as_view()),
]