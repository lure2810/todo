from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import todomodel
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):
  template_name = 'list.html'
  model = todomodel

class TodoDetail(DetailView):
  template_name = 'detail.html'
  model = todomodel

class TodoCreate(CreateView):
  template_name = 'create.html'
  model = todomodel
  fields = ('title','memo','priority','duedata')
  success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
  template_name = 'delete.html'
  model = todomodel
  success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
  template_name = 'update.html'
  model = todomodel
  fields = ('title','memo','priority','duedata')
  success_url = reverse_lazy('list')