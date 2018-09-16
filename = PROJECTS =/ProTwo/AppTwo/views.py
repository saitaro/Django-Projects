from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User, Mail
from AppTwo.forms import NewUserForm

# Create your views here.
def index(request):
    return HttpResponse('Hello')

def help(request):
    helpdict = {'help_insert': 'HELPING PAGING'}
    return render(request, 'Apptwo/help.html', context=helpdict)

def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return help(request)
        else:
            print('Error: form invalid')
    
    return render(request, 'AppTwo/users.html', {'form': form})

def newpage(request, ok):
    print(ok)

    NewDict = {'lusie': 'red', 'jordan': 'blue', 'maiden': 'green'}

    return render(request, 'AppTwo/mynewpage.html', context=NewDict)

    # userlist = {
        
    #     'userlist': User.objects.all(), 
    #     'maillist': Mail.objects.order_by('owner')
    # }
    
    # return render(request, 'Apptwo/users.html', context=userlist)