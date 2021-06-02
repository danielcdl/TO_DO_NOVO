from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Grupo


class VerGrupo(LoginRequiredMixin, View):

    def get(self, request, slug_grupo):
        busca = request.GET.get('busca', '')
        grupo = get_object_or_404(Grupo, slug=slug_grupo)
        subgrupos = grupo.subgrupo_set.all()

        if busca:
            subgrupos = subgrupos.filter(nome__icontains=busca)

        context = {'grupo': grupo, 'subgrupos': subgrupos, 'busca': busca}

        return render(request, "grupo/grupo.html", context)


class CriarGrupo(LoginRequiredMixin, CreateView):
    model = Grupo
    context_object_name = 'criar_grupo'
    success_url = reverse_lazy('home:index')
    fields = ('nome',)
    template_name = 'grupo/formulario_grupo.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CriarGrupo, self).form_valid(form)


class AtualizarGrupo(LoginRequiredMixin, UpdateView):
    model = Grupo
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/formulario_grupos.html'


class ApagarGrupo(LoginRequiredMixin, DeleteView):
    model = Grupo
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/apagar_grupo.html'
