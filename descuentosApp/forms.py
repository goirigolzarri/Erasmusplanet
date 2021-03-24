from django import forms
from .models import *


choices_city = City.objects.all().values_list('name', 'name')
city_list = []

for item in choices_city:
	city_list.append(item)

class AñadirGuia(forms.ModelForm):

    class Meta:
        model = Guide
        fields = ('city', 'title', 'imagen_informacion_general', 'informacion_general','como_llegar', 'comida',
         'alojamiento', 'ocio', 'divisas', 'banco_sim', 'donde_comprar')

        widgets ={
			
            'city': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'title': forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'informacion_general': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'como_llegar': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'comida':forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'alojamiento': forms.Textarea(attrs={'class':'form-control ', 'value': '', 'type': 'hidden'}),
			'ocio': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'divisas': forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'banco_sim': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'donde_comprar': forms.Textarea(attrs={'class':'form-control ', 'placeholder': 'First name...'}),
			


        }

class EditarGuia(forms.ModelForm):

    class Meta:
        model = Guide
        fields = ('city', 'title','informacion_general','como_llegar', 'comida',
         'alojamiento', 'ocio', 'divisas', 'banco_sim', 'donde_comprar')

        widgets ={
			
            'city': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'title': forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'informacion_general': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'como_llegar': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'comida':forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'alojamiento': forms.Textarea(attrs={'class':'form-control ', 'value': '', 'type': 'hidden'}),
			'ocio': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'divisas': forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'banco_sim': forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Añadir titulo de guia..'}),
			'donde_comprar': forms.Textarea(attrs={'class':'form-control ', 'placeholder': 'First name...'}),
			


        }
