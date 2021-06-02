from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from grupo.models import Grupo
from subgrupo.models import SubGrupo
from tarefa.models import Tarefa


class Index(LoginRequiredMixin, View):

    def get(self, request):

        incompletas = len(Tarefa.objects.filter(complete=False))

        return render(request, "home/index.html", {'incompletas': incompletas})



class Grupos(LoginRequiredMixin, View):

    def get(self, request):
        busca = request.GET.get('busca', '')
        grupos = Grupo.objects.filter(user=request.user)
        if busca:
            grupos = grupos.filter(nome__icontains=busca)

        context = {'grupos': grupos, 'busca': busca}

        return render(request, "home/grupos.html", context)


class SubGrupos(LoginRequiredMixin, View):

    def get(self, request):
        busca = request.GET.get('busca', '')
        subgrupos = SubGrupo.objects.filter(user=request.user)
        if busca:
            subgrupos = subgrupos.filter(nome__icontains=busca)

        context = {'subgrupos': subgrupos, 'busca': busca}

        return render(request, "home/subgrupos.html", context)


class Tarefas(LoginRequiredMixin, View):

    def get(self, request):
        busca = request.GET.get('busca', '')
        tarefas = Tarefa.objects.filter(user=request.user)
        if busca:
            tarefas = tarefas.filter(nome__icontains=busca)

        context = {'tarefas': tarefas, 'busca': busca}

        return render(request, "home/tarefas.html", context)