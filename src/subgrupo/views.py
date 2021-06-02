from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.views.generic.list import ListView
from django.views.generic import CreateView, View
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from grupo.models import Grupo

from .forms import SubGrupoForm
from .models import SubGrupo

class CriarSubGrupo(LoginRequiredMixin, View):
    template_name = 'subgrupo/formulario_subgrupo.html'
    form_model = SubGrupoForm
    
    def get(self, request, slug_grupo):
        form = self.form_model(request.GET)
        return render(request, self.template_name, {'form': form, 'slug_grupo': slug_grupo})

    def post(self, request, slug_grupo):

        grupo = get_object_or_404(Grupo, slug=slug_grupo)
        form = self.form_model(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.grupo = grupo
            formulario.user = request.user
            formulario.save()
            return redirect(f'/{grupo.slug}/')
        else:
            return render(request, self.template_name, {'form': form, 'slug_grupo': slug_grupo})

class VisualizarSubGrupo(LoginRequiredMixin, ListView):

    def get(self, request, slug_grupo, slug_subgrupo):
        busca = request.GET.get('search-area', '')
        subgrupo = get_object_or_404(SubGrupo, slug=slug_subgrupo, grupo__slug=slug_grupo)
        tarefas = subgrupo.tarefa_set.all()

        if busca:
            tarefas = tarefas.filter(nome___icontains=busca)

        context = {'tarefas': tarefas, 'subgrupo': subgrupo, 'search_input': busca}

        return render(request, "subgrupo/subgrupo.html", context)


class MostraSubGrupo(LoginRequiredMixin, View):

    def get(self, request, pk):
        subgrupo_especifico = SubGrupo.objects.get(id=pk)
        join_subgrupo = subgrupo_especifico.tarefa_subgrupos.all()
        id_grupo = subgrupo_especifico.grupo_sub_id

        busca = request.GET.get('search-area', '')

        if busca:
            join_subgrupo = join_subgrupo.filter(title__icontains=busca)

        context = {'join_subgrupo': join_subgrupo, 'pk': pk, 'search_input': busca, 'id_grupo': id_grupo}

        return render(request, "login/mostra_subgrupo.html", context)




def exclui_subgrupo(request, pk):
    item = SubGrupo.objects.get(id=pk)
    id_grupo = item.grupo_sub_id

    if request.method == 'POST':
        item.delete()
        return redirect(f'/subgrupos/{id_grupo}')

    return render(request, 'login/apagar_subgrupo.html', {'pk': pk, 'id_grupo': id_grupo})


def edita_subgrupo(request, pk):
    item_id = SubGrupo.objects.get(id=pk)
    id_grupo = item_id.grupo_sub_id

    if request.method == 'POST':
        item = get_object_or_404(SubGrupo, id=pk)
        form = SubGrupoForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect(f'/subgrupos/{id_grupo}')
    else:
        item = SubGrupo.objects.filter(id=pk).values().last()
        form = SubGrupoForm(initial=item)

    return render(request, 'login/formulario_subgrupos.html', {'pk': pk, 'form': form, 'id_grupo': id_grupo})


def atualiza_subgrupo(request, pk):
    item = SubGrupo.objects.get(id=pk)
    id_grupo = item.grupo_sub_id

    if request.method == 'POST':
        item.delete()
        return redirect(f'/subgrupos/{id_grupo}')

    return render(request, 'login/apagar_subgrupo.html', {'pk': pk, 'id_grupo': id_grupo})


class AtualizarSubGrupo(LoginRequiredMixin, UpdateView):
    model = SubGrupo
    fields = '__all__'
    template_name = 'login/formulario_subgrupos.html'
