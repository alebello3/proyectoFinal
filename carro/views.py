from django.shortcuts import render

# Create your views here.
from .carro import carro
from tienda.models import producto
from django.shortcuts import redirect


def agregar_vista(request, producto_id):
    carro=carro(request)
    producto=producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)
    return redirect("tienda")

def eliminar_vista(request, producto_id):
    carro=carro(request)
    producto=producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)
    return redirect("tienda")

def restarr_producto(request, producto_id):
    carro=carro(request)
    producto=producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)
    return redirect("tienda")

def limpiar_carro(request, producto_id):
    carro=carro(request)
    carro.limpiar_carro()
    return redirect("tienda")


