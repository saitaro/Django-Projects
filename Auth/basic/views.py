from django.shortcuts import render
from . import models
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    View, 
    TemplateView, 
    ListView, 
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
    
class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    model = models.School
    context_object_name = 'school_detail'
    template_name = 'basic/school_detail.html'

# Create your views here.

class IndexView(TemplateView):
    template_name = 'basic/main.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['mypoint'] = 'Bitchplace!'
    #     return context

class RegisterView(TemplateView):
    template_name = 'basic/registration.html'

class SchoolCreateView(CreateView):
    fields = (
        'name',
        'principal',
        'location'
    )
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = (
        'name',
        'principal'
    )
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic:list")