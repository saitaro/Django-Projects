from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy 
from django.views.generic import (  TemplateView, 
                                    ListView, 
                                    CreateView,
                                    DetailView,
                                    UpdateView,
                                    DeleteView
                                )
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    
class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'cbviews/school_detail.html'
    context_object_name = 'school_detail'
    
class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('cbviews:list')




