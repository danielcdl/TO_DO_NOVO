from django.urls import path

from .views import Index, Grupos, SubGrupos, Tarefas


app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('grupos/', Grupos.as_view(), name='grupos'),
    path('subgrupos/', SubGrupos.as_view(), name='subgrupos'),
    path('tarefas/', Tarefas.as_view(), name='tarefas'),
]
