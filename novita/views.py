from django.shortcuts import render
from .models import Novita

# Create your views here.

from django.http import HttpResponse
import datetime

from django.template import RequestContext

def list(request):
    novita = Novita.objects.all()
    return  render(request, 'lista_novita.html', {'novita': novita})