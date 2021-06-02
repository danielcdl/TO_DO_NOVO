from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import UpdateView, DeleteView

from grupo.models import Grupo
from subgrupo.models import SubGrupo

from .models import Tarefa
from .forms import TarefaForm


class CriarTarefa(LoginRequiredMixin, View):
    template_name = 'tarefa/criar_tarefa.html'
    form_model = TarefaForm
    
    def get(self, request, slug_grupo, slug_subgrupo):
        
        form = self.form_model(request.GET)
        return render(request, self.template_name, {'form': form, 'slug_grupo': slug_grupo, 'slug_subgrupo': slug_subgrupo})

    def post(self, request, slug_grupo, slug_subgrupo):

        grupo = get_object_or_404(Grupo, slug=slug_grupo)
        subgrupo = get_object_or_404(SubGrupo, slug=slug_subgrupo)
        form = self.form_model(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.grupo = grupo
            formulario.subgrupo = subgrupo
            formulario.user = request.user
            formulario.save()
            return redirect('subgrupo:subgrupo', slug_grupo, slug_subgrupo)
        else:
            return render(request, self.template_name, {'form': form, 'slug_grupo': slug_grupo})


class EditarTarefa(LoginRequiredMixin, View):

    template_name = 'tarefa/editar_tarefa.html'
    model_form = TarefaForm

    def get(self, request, slug_grupo, slug_subgrupo, pk):
        grupo = get_object_or_404(Grupo, slug=slug_grupo)
        subgrupo = get_object_or_404(SubGrupo, slug=slug_subgrupo)
        tarefa = get_object_or_404(Tarefa, grupo=grupo, subgrupo=subgrupo, id=pk)
        form = self.model_form(instance=tarefa)
        
        return render(request, self.template_name, {'form': form, 'grupo':slug_grupo, 'subgrupo': slug_subgrupo})

    def post(self, request, slug_grupo, slug_subgrupo, pk):
        grupo = get_object_or_404(Grupo, slug=slug_grupo)
        subgrupo = get_object_or_404(SubGrupo, grupo=grupo, slug=slug_subgrupo)
        tarefa = get_object_or_404(Tarefa, grupo=grupo, subgrupo=subgrupo, id=pk)
        
        form = self.model_form(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('subgrupo:subgrupo', slug_grupo, slug_subgrupo)
        else:
            return render(request, self.template_name, {'form': form})

class ExcluirTarefa(LoginRequiredMixin, View):

    template_name = 'tarefa/excluir_tarefa.html'
    model_form = TarefaForm

    def get(self, request, slug_grupo, slug_subgrupo, pk):
        grupo = get_object_or_404(Grupo, slug=slug_grupo)
        subgrupo = get_object_or_404(SubGrupo, slug=slug_subgrupo)
        tarefa = get_object_or_404(Tarefa, grupo=grupo, subgrupo=subgrupo, id=pk)
        
        return render(request, self.template_name, {'tarefa': tarefa, 'grupo': slug_grupo, 'subgrupo': slug_subgrupo})

    def post(self, request, slug_grupo, slug_subgrupo, pk):
        grupo = get_object_or_404(Grupo, slug=slug_grupo)
        subgrupo = get_object_or_404(SubGrupo, grupo=grupo, slug=slug_subgrupo)
        tarefa = get_object_or_404(Tarefa, grupo=grupo, subgrupo=subgrupo, id=pk)
        
        tarefa.delete()

        return redirect('subgrupo:subgrupo', slug_grupo, slug_subgrupo)

   