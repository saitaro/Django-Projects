from django.shortcuts import render
from .forms import TicketForm
from .models import Ticket

# Create your views here.
def index(request):

    context = {
        'form': TicketForm(),
        'items': Ticket.objects.all()
    }
    
    if request.method == 'POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'base.html', context)
        else:
            print('Form is not valid.')

    return render(request, 'base.html', context)
