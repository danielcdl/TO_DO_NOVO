from django.forms import ModelForm
from .models import Grupos, Tarefa, Sub_Grupos

class GruposForm(ModelForm):
    class Meta:
        model = Grupos
        fields = '__all__'

class TarefasForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['title', 'description', 'complete']


class Sub_GruposForm(ModelForm):
    class Meta:
        model = Sub_Grupos
        fields = ['nome_subgrupo']