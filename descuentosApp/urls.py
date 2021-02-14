from django.urls import path
from . import views


urlpatterns = [

	path('',views.base, name='base'),
	path('city-list/', views.CityList, name='CityList'),
	path('descuentos/', views.Descuentos, name='Descuentos'),
	path('alojamiento/', views.Alojamiento, name='Alojamiento'), 
    path('adminsite/', views.AdminSite, name='Admin'), 
    path('adminsite/addguide', views.AddGuide.as_view(), name='AddGuide'), 
	path('guia/', views.Guia, name='Guia'),
    

]