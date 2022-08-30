from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import *
from .models import *

#==============================CREATE====================================

class AutorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Autor
    form_class = AutorForm
    template_name = "form.html"
    success_url = reverse_lazy("listar_autores")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Autores'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class CursoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Curso
    form_class = CursoForm
    template_name = "form.html"
    success_url = reverse_lazy("listar_cursos")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Cursos'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Orientador
    form_class = OrientadorForm
    template_name = "form.html"
    success_url = reverse_lazy("listar_orientadores")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientadores'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class TccCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tcc
    form_class = TccForm
    template_name = "form.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tccs'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

#===================================UPDATE=================================

class AutorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Autor
    form_class = AutorForm
    template_name = "form.html"
    success_url = reverse_lazy("listar_autores")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Autores'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class CursoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Curso
    form_class = CursoForm
    template_name = "form.html"
    success_url = reverse_lazy("listar_cursos")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Cursos'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Orientador
    form_class = OrientadorForm
    template_name = "form.html"
    success_url = reverse_lazy("listar_orientadores")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientadores'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class TccUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tcc
    form_class = TccForm
    template_name = "form.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tccs'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

#===================================LIST====================================
class AutorList(LoginRequiredMixin, ListView):
    model = Autor
    template_name = "list/autores.html"

class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "list/cursos.html"
    
class OrientadorList(LoginRequiredMixin, ListView):
    model = Orientador
    template_name = "list/orientadores.html"

class TccList(ListView):
    model = Tcc
    template_name = "index.html"

#=================================DELETE=====================================
class AutorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Autor
    template_name = "form-excluir.html"
    success_url = reverse_lazy("listar_autores")

class CursoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Curso
    template_name = "form-excluir.html"
    success_url = reverse_lazy("listar_cursos")

class OrientadorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Orientador
    template_name = "form-excluir.html"
    success_url = reverse_lazy("listar_orientadores")

class TccDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Tcc
    template_name = "form-excluir.html"
    success_url = reverse_lazy("index")

#================================DETAIL=======================================
class TccDetail(DetailView):
    model = Tcc
    template_name = "detail/tcc.html"
