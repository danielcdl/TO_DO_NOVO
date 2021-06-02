from django.forms import ModelForm
from .models import Tarefa


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['title', 'description', 'complete']
