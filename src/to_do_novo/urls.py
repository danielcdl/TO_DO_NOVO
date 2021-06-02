from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('', include('grupo.urls')),
    path('admin/', admin.site.urls),
    path('conta/', include('conta.urls')),
    path('<slug_grupo>/', include('subgrupo.urls')),
    path('<slug_grupo>/<slug_subgrupo>/', include('tarefa.urls')),
]
