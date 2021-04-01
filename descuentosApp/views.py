from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from .models import Guide, City
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.db.models import Q
from .forms import AñadirGuia, EditarGuia


# Create your views here.


	
def base(request):

	#from django.utils import translation
	#user_language = 'es'
	#translation.activate(user_language)
	#request.session[translation.LANGUAGE_SESSION_KEY] = user_language
	#if translation.LANGUAGE_SESSION_KEY in request.session:
	#del request.session[translation.LANGUAGE_SESSION_KEY]
	
	model = Guide
	city_list = City.objects.all()
	guiasTarjetas = Guide.objects.all()


	queryset= request.GET.get("search")
	guides = Guide.objects.all()
	query = False
	errormessage='Todavia no trabajamos ahi'

	if queryset:
		
		
		guides = Guide.objects.filter(Q(title__icontains = queryset)).distinct()
		if not guides:
			query = True
		else: 
			context = {'guides': guides}
			query = True
		


	return render(request, 'base.html', {'guides': guides, 'query' : query, 'guiasTarjetas': guiasTarjetas})



def CityList(request):

	city_list = City.objects.all()
	return render(request, 'city_list.html', {'city_list': city_list})

def Descuentos(request):
        
    return render(request, 'descuentos.html')

def Alojamiento(request):
        
    return render(request, 'alojamiento.html')


def AdminSite(request):

    guides = Guide.objects.all()
    context = {'guides': guides}

    return render(request, 'admin.html', context)

class AddGuide(CreateView):
	model = Guide
	form_class = AñadirGuia
	template_name = 'add_guide.html'

	success_url = reverse_lazy('Admin')

class EditGuide(UpdateView):
	model = Guide
	form_class = EditarGuia
	template_name = 'edit_guide.html'

	success_url = reverse_lazy('Admin')

class DeleteGuide(DeleteView):

	model = Guide
	template_name = 'delete_guide.html'
	success_url = reverse_lazy('Admin')



class Guia(DetailView):
    
	model = Guide
	template_name = 'guia.html'




def Tienda(request):

    return render(request, 'tienda.html')

def Carrito(request):

    return render(request, 'carrito.html')

def Contacto(request):

	return render(request, 'contacto.html')

def Propuestaguia(request):

	return render(request, 'Propuestaguia.html')