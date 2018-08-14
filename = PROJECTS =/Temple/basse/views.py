from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'simple': 'here i am',
         'lucky': 100
    }
    return render(request, 'basse/index.html', context)

def other(request):
    return render(request, 'basse/other.html')

def relative(request):
    return render(request, 'basse/relative_url_templates.html')
