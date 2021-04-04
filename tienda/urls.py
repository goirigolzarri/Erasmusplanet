from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [


    path('tienda/', views.Tienda, name='Tienda'),
	path('carrito/', views.Carrito, name='Carrito'),

    
]