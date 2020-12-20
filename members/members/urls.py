from django.urls import path
from . import views


urlpatterns = [


	path('members/',views.UserRegistrationView.as_view(), name='UserRegistrationView'),
	path('login/', views.Login, name='Login'),

]