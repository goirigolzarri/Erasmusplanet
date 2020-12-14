from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth  import authenticate, login, logout






class UserRegistrationView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/registration.html'
	success_url = reverse_lazy('login')


def Login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('base')

	return render(request, 'registration/login.html')


 
