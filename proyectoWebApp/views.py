from django.shortcuts import render, HttpResponse
from carro.carro import Carro
from servicios.models import Servicio

# Create your views here.

def home (request):
    carro=Carro(request)
    return render(request, "proyectoWebApp/home.html")

def nosotros (request):
    return render(request, "proyectoWebApp/nosotros.html")



