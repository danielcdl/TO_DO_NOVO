from django.urls import path, include
from .views import VisualizarSubGrupo, MostraSubGrupo, CriarSubGrupo, exclui_subgrupo, edita_subgrupo

app_name = 'subgrupo'

urlpatterns = [
    path('subgrupo/criar/', CriarSubGrupo.as_view(), name='criar'),
    path('atualizar/<slug_subgrupo>/', edita_subgrupo, name='atualizar'),
    path('apagar/<slug_subgrupo>/', exclui_subgrupo, name='apagar'),
    path('mostra/<slug_subgrupo>/', MostraSubGrupo.as_view(), name='mostra'),
    path('<slug_subgrupo>/', VisualizarSubGrupo.as_view(), name='subgrupo'),
]
