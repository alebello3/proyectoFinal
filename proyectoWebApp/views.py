from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.

def home (request):
    return render(request, "proyectoWebApp/home.html")

def nosotros (request):
    return render(request, "proyectoWebApp/nosotros.html")



