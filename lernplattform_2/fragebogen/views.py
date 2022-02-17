from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.

class FragebogenHome(ListView):
    model = Fragebogen
    template_name = 'fragebogen/fragebogen_home.html'
