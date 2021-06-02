from django.forms import ModelForm
from .models import SubGrupo

class SubGrupoForm(ModelForm):
    class Meta:
        model = SubGrupo
        fields = ['nome']