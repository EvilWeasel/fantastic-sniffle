from django.shortcuts import render

from .models import Fragebogen

# Create your views here.


def index(request):
    return render(request, 'index.html')


def fragebogen(request):
    bogen = Fragebogen.objects.all()
    return render(request, 'fragebogen_liste.html', {'bogen': bogen})
