from django.urls import path
from .views import CriarTarefa, EditarTarefa, ExcluirTarefa


app_name = 'tarefa'

urlpatterns = [
    path('tarefa/criar/', CriarTarefa.as_view(), name='criar'),
    path('<int:pk>/atualizar/', EditarTarefa.as_view(), name='atualizar'),
    path('<int:pk>/apagar/', ExcluirTarefa.as_view(), name='apagar'),
]
