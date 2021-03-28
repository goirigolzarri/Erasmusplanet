from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [

	path('',views.base, name='base'),
	path('city-list/', views.CityList, name='CityList'),
	path('descuentos/', views.Descuentos, name='Descuentos'),
	path('alojamiento/', views.Alojamiento, name='Alojamiento'), 
    path('adminsite/', views.AdminSite, name='Admin'), 
    path('adminsite/addguide', views.AddGuide.as_view(), name='AddGuide'), 
	path('guia/<int:pk>', views.Guia.as_view(), name='Guia'),
	path('adminsite/editguide/<int:pk>', views.EditGuide.as_view(), name='EditGuide'),
    path('adminsite/deleteguide/<int:pk>', login_required(views.DeleteGuide.as_view()), name='DeleteGuide'),
    
    path('tienda/', views.Tienda, name='Tienda'),
	path('carrito/', views.Carrito, name='Carrito'),

]