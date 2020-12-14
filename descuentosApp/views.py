from django.shortcuts import render
from django.http import HttpResponse
from .models import Guide, City
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView
# Create your views here.


	

def base(request):

	#from django.utils import translation
	#user_language = 'es'
	#translation.activate(user_language)
	#request.session[translation.LANGUAGE_SESSION_KEY] = user_language
	#if translation.LANGUAGE_SESSION_KEY in request.session:
	#del request.session[translation.LANGUAGE_SESSION_KEY]
	
	city_list = City.objects.all()

	return render(request, 'base.html', {'city_list': city_list})





class GuideDetailView(DetailView):
	model = Guide
	template_name='guide_detail.html'

def CityList(request):

	city_list = City.objects.all()
	return render(request, 'city_list.html', {'city_list': city_list})



def Descuentos(request):
        
    return render(request, 'descuentos.html')


#def Progress_bar_register(request):

#	return render(request, 'progress_bar_register.html')