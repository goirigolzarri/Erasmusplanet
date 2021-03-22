from django.urls import path
from . import views
from .views import *


urlpatterns = [


	path('register/', NewUserRegistrationView.as_view(), name='UserRegistrationView'),
	path('register2/', NewUserRegistrationView2.as_view(), name='UserRegistrationView2'),

	path('login/', views.Login, name='Login'),
   # path('register/', views.Register, name='Register'),

]