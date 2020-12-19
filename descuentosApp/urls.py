from django.urls import path
from . import views


urlpatterns = [

	path('',views.base, name='base'),
	path('guide/<int:pk>/', views.GuideDetailView.as_view(), name = 'GuideDetailView'),
	path('city-list/', views.CityList, name='CityList'),
	path('descuentos/', views.Descuentos, name='Descuentos'),
	path('alojamiento/', views.Alojamiento, name='Alojamiento'), 
	#path('registrer/', views.Progress_bar_register, name='registrer')

]