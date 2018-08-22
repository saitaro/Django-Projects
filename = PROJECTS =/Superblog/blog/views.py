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

    def func_1(self):
        1

    def func_2(self):
        2
        
    def func_3(self):
        3
    
    def func_4(self):
        4