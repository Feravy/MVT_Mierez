from datetime import datetime
from pyexpat import model
from django.shortcuts import render
from MVT_Mierez.models import Persona

# Create your views here.

def familiar1(request):

    year= 1958
    month= 1
    day= 10
    familiar1 = Persona(nombre = "Delia",
    dni = "12713789",
    fecha_nacimiento= datetime(year=year, month=month, day=day),
    edad = 64)
    familiar1.save
    contexto = {
        'familiar1': familiar1
    }

    return render(request, 'familiar1.html', contexto)

def familiar2(request):

    year= 1988
    month= 10
    day= 21
    familiar2 = Persona(nombre = "Fernanda",
    dni = "33567310",
    fecha_nacimiento= datetime(year=year, month=month, day=day),
    edad = 33)
    familiar2.save
    contexto = {
        'familiar2': familiar2
    }

    return render(request, 'familiar2.html', contexto)

def familiar3(request):

    year= 1996
    month= 5
    day= 14
    familiar3 = Persona(nombre = "Rodrigo",
    dni = "39647709",
    fecha_nacimiento= datetime(year=year, month=month, day=day),
    edad = 26)
    familiar3.save
    contexto = {
        'familiar3': familiar3
    }

    return render(request, 'familiar3.html', contexto)