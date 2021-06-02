from django.urls import path
from .views import Logar, Registrar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Logar.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registrar/', Registrar.as_view(), name='registrar'),
]
