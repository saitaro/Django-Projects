from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me': 'Coming from firstApp/index.html'}
    return render(request, 'firstApp/index.html', context=my_dict)