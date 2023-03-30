from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.

def home (request):
    return render(request, "proyectoWebApp/home.html")

def nosotros (request):
    return render(request, "proyectoWebApp/nosotros.html")

def servicios (request):
    servicios= Servicio.objects.all()
    return render(request, "proyectoWebApp/servicios.html",{"servicios":servicios})

def tienda (request):
    return render(request, "proyectoWebApp/tienda.html")

def blog (request):
    return render(request, "proyectoWebApp/blog.html")

def contacto (request):
    return render(request, "proyectoWebApp/contacto.html")