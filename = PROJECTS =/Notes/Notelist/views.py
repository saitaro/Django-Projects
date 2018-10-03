from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, TemplateView,
								  DeleteView, ListView, UpdateView)
from .models import Note
from .forms import NoteForm
from django.urls import reverse_lazy, reverse


class NoteView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwards):
  		context = Note.objects.all()
  		return {'notes': context}
  		

class NoteCreateView(CreateView):
	model = Note
	form_class = NoteForm
	# fields = '__all__'
	template_name = '../templates/note_form.html'
	success_url= '/'
	

class NoteListView(ListView):
	model = Note


class NoteDeleteView(DeleteView):
	model = Note
	template_name = '../templates/note_delete.html'
	success_url = '/'


class NoteUpdateView(UpdateView):
	model = Note
	form_class = NoteForm
	template_name = '../templates/note_form.html'
	success_url = '/'


class NoteDetailView(DetailView):
	model = Note
	form_class = NoteForm
	template_name = '../templates/note_detail.html'