from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from . import models
from django.core.urlresolvers import reverse_lazy, reverse

class GroceryList(ListView):
    model = models.Task
    context_object_name = 'groceries'
    template_name = 'tasklist/complete.html'

class GroceryCreate(CreateView):
    model = models.Task
    fields = (
        'title',
        'text',
    )
    success_url = '/'

class GroceryDelete(DeleteView):
    model = models.Task
    success_url = reverse_lazy('tasklist:mainlist')

class GroceryDetail(DetailView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'tasklist/task_detail.html'
