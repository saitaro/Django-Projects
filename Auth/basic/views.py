from django.shortcuts import render
from . import models
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
    # template_name = 'basic/school_form.html'
    fields = (
        'name',
        'principal',
        'location'
    )
    model = models.School