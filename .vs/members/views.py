from descuentosApp.models import Country
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm, CreateUserForm
from django.contrib.auth  import authenticate, login, logout






class NewUserRegistrationView(generic.CreateView):
	
    form_class = CreateUserForm
    model = Country
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')



def Login(request):

    form_class = UserCreationForm()
    if request.method == 'POST':

        if request.POST.get('submit') == 'sign_in':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('base')

        elif request.POST.get('submit') == 'sign_up':

            context = {}
            form_class = UserCreationForm(request.POST or None)
            if request.method == "POST":
                if form.is_valid():
                    user = form.save()
                    login(request,user)
                    return render(request,'accounts/index.html')
            context['form']=form



    return render(request, 'registration/login.html', context)


 



 

class NewUserRegistrationView2(generic.CreateView):
    
    form_class = CreateUserForm
    template_name = 'registration/registration2.html'
    success_url = reverse_lazy('login')
