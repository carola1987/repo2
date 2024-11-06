from django.shortcuts import render
from django.http import HttpResponse
from .models import flan


# Create your views here.
def algo(request):
    return HttpResponse('OnlyFlans')

def home(request):
    return render(request, 'home.html', {})

def acerca(request):
    return render(request, 'acerca.html', {})

def bienvenido(request):
    return render(request, 'bienvenido.html', {})

def inicio(request):
    return render(request, 'inicio.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def index(request):
    flanes = flan.objects.all()
    return render(request, 'index.html', {'flan': flan })
