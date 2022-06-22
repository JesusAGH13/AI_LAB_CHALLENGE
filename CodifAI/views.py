from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Por favor seleccione el lenguaje que desea clasificar")
