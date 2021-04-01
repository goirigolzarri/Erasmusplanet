from django.contrib.auth.decorators import login_required
from descuentosApp.models import Country
from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth.forms import *
from django.urls import reverse_lazy
from .forms import *
from .models import User
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView






class NewUserRegistrationView(CreateView):
	
    form_class = CreateUserForm
    model = Country
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')



def Login(request):

  
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


 



 

class NewUserRegistrationView2(CreateView):
    
    form_class = CreateUserForm
    template_name = 'registration/registration2.html'
    success_url = reverse_lazy('login')

@login_required
def UserProfile(request):

    return render(request, 'profile/userProfile.html')


class EditProfile(UpdateView):

    form_class = EditUserForm
    template_name = 'profile/edit_profile.html'
    success_url = reverse_lazy('base') #METER PLANTILLA DE SUCCESFULL EDIT.
    
    

    def get_object(self):
        return self.request.user



class PasswordChangeView(PasswordChangeView):

    form_class = ChangePassword
    template_name = 'perfil/change_password.html'
    succes_url = reverse_lazy('Index')
    
