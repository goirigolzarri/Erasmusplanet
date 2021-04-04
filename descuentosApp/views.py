from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from .models import Guide, City
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.db.models import Q
from .forms import AñadirGuia, ContactForm, EditarGuia
from django.template.loader import get_template
from django.core.mail import EmailMessage


# Create your views here.


def base(request):

	# from django.utils import translation
	# user_language = 'es'
	# translation.activate(user_language)
	# request.session[translation.LANGUAGE_SESSION_KEY] = user_language
	# if translation.LANGUAGE_SESSION_KEY in request.session:
	# del request.session[translation.LANGUAGE_SESSION_KEY]

	model = Guide
	city_list = City.objects.all()
	guiasTarjetas = Guide.objects.all()

	queryset = request.GET.get("search")
	guides = Guide.objects.all()
	query = False
	errormessage = 'Todavia no trabajamos ahi'

	if queryset:

		guides = Guide.objects.filter(Q(title__icontains=queryset)).distinct()
		if not guides:
			query = True
		else:
			context = {'guides': guides}
			query = True

	return render(request, 'base.html', {'guides': guides, 'query': query, 'guiasTarjetas': guiasTarjetas})


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






def Contacto(request):

	form = ContactForm()
	context = {'form': form}

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():

			firstname = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			subject = request.POST.get('subject')
			body = request.POST.get('body')

			context = {
				'firstname': firstname,
				'last_name': last_name,
				'email': email,
				'subject': subject,
				'body': body,
			}
			template = get_template('contacto.txt')
			
			content = template.render(context)

			email = EmailMessage(
                "Contact Page / " + subject,
                content,
                "Erasmus Planet" +'',
                ['erasmuusplanet@gmail.com'],
                headers = {'Reply-To': email }
            )
			email.send()
			
			return redirect('Contacto')







	return render(request, 'contacto.html', context)

def Propuestaguia(request):

	
	return render(request, 'propuestaguia.html')
