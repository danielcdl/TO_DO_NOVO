from .models import Tarefa, Grupos, Sub_Grupos
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#Bloco Autenticação
class Logar(LoginView):
    template_name = 'login/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('grupos')

class Registrar(FormView):
    template_name = 'login/registrar.html'
    fields = '__all__'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tarefas')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registrar, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tarefas')
        return super(Registrar, self).get(*args, **kwargs)

class Sair(LogoutView):

    def get_success_url(self):
        return reverse_lazy('login')


#Bloco Tratamento Grupos
class VisualizaGrupo(LoginRequiredMixin, ListView, View):

    def get(self, request):
        grupos = Grupos.objects.all()
        context = {'grupos': grupos}

        return render(request, "login/grupos.html", context)

class CriarGrupo(LoginRequiredMixin, CreateView):
    model = Grupos
    context_object_name = 'criar_grupo'
    success_url = reverse_lazy('grupos')
    fields = '__all__'
    template_name = 'login/formulario_grupos.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CriarGrupo, self).form_valid(form)

class AtualizarGrupo(LoginRequiredMixin, UpdateView):
    model = Grupos
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/formulario_grupos.html'

class ApagarGrupo(LoginRequiredMixin, DeleteView):
    model = Grupos
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/apagar_grupo.html'



#Bloco Tratamento Sub_Grupo
class VisualizaSubGrupo(LoginRequiredMixin, ListView):

    def get(self, request, pk):
        grupo_especifico = Grupos.objects.get(id=pk)
        print(grupo_especifico)
        join_subgrupo = grupo_especifico.join_grupos.all()
        print(join_subgrupo)
        context = {'join_subgrupo': join_subgrupo}

        return render(request, "login/subgrupos.html", context)

class MostraSubGrupo(LoginRequiredMixin, View):

    def get(self, request, pk):
        subgrupo_especifico = Sub_Grupos.objects.get(id=pk)
        join_subgrupo = subgrupo_especifico.tarefa_subgrupos.all()
        context = {'join_subgrupo': join_subgrupo}
        return render(request, "login/mostra_subgrupo.html", context)

class CriarSubGrupo(LoginRequiredMixin, CreateView):
    model = Sub_Grupos
    context_object_name = 'criar_subgrupo'
    fields = '__all__'
    template_name = 'login/formulario_subgrupos.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CriarSubGrupo, self).form_valid(form)

class AtualizarSubGrupo(LoginRequiredMixin, UpdateView):
    model = Sub_Grupos
    fields = '__all__'
    template_name = 'login/formulario_subgrupos.html'

class ApagarSubGrupo(LoginRequiredMixin, DeleteView):
    model = Sub_Grupos
    fields = '__all__'
    success_url = reverse_lazy('subgrupos')
    template_name = 'login/apagar_subgrupo.html'



#Bloco Tratamento Tarefas
class ListaTarefa(LoginRequiredMixin, ListView):
    model = Tarefa
    fields = '__all__'
    context_object_name = 'tarefas'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tarefas'] = data['tarefas'].filter(user=self.request.user)
        data['count'] = data['tarefas'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            data['tarefas'] = data['tarefas'].filter(
                title__startswith=search_input)
        data['search_input'] = search_input
        return data

class TodasTarefas(LoginRequiredMixin, ListView):
    model = Tarefa
    context_object_name = 'completo'

class Criar(LoginRequiredMixin, CreateView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/formulario.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Criar, self).form_valid(form)

class Atualizar(LoginRequiredMixin, UpdateView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/formulario.html'

class Apagar(DeleteView, LoginRequiredMixin):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/confirmar.html'