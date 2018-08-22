from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
)

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))
    
    def new_shit(self):
        return second_shit 2233321 bla bla