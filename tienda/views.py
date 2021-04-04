from django.shortcuts import render
from .models import *

# Create your views here.
def Carrito(request):

    return render(request, 'carrito.html')


def Tienda(request):

	productos = Producto.objects.all()

	context = {'productos': productos}

	return render(request, 'clientes/tienda.html', context)

