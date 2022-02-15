from queue import Empty
from django.shortcuts import render

from .models import Fragebogen

# Create your views here.


def index(request):
    return render(request, 'index.html')


def fragebogen(request):
    bogen = Fragebogen.objects.all()
    return render(request, 'fragebogen_liste.html', {'bogen': bogen})


def fragebogenDetails(request, pk):
    bogen = Fragebogen.objects.get(id=pk)
    return render(request, 'fragebogen_details.html', {'bogen': bogen})
