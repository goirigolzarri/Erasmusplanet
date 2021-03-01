from descuentosApp.models import Country
from django.contrib.auth.forms import UserCreationForm

from members.models import User
from django import forms
from .models import City, Country




# Cargar SubCategorias
choices_sub = City.objects.all().values_list('name', 'name')
city_list = []

for item in choices_sub:
	city_list.append(item)


choices_country = Country.objects.all().values_list('name', 'name')
country_list = []

for item in choices_country:
	country_list.append(item)

#generos
gender_list=['Male ', 'Female', 'Unisex']
studentType_list=['Academic ', 'Au Pair', 'Master', 'Practices']

class SignUpForm(UserCreationForm):
	email =forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','city', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
			  
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'



class CreateUserForm(UserCreationForm):
	
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'date' , 'gender' ,'country', 'phone', 'studentType', 'cityOrigin1',
		 'cityDestination1', 'cityDestination2', 'cityDestination3', 'universityOrigin', 'universityDestination', 'studies', 'email', 'password1', 'password2', 'course', 'company']
		
			  

		widgets ={
            'cityDestination1': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'cityDestination2': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'cityDestination3': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'cityOrigin1': forms.Select(choices=city_list, attrs={'class':'form-control '}),
			'universityOrigin': forms.Select(attrs={'class':'form-control '}),
			'universityDestination': forms.Select(attrs={'class':'form-control '}),
			'country': forms.Select(choices=country_list, attrs={'class':'form-control ', 'default':False}),
			'gender': forms.Select(choices=gender_list, attrs={'class':'form-control '}),
			'first_name': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'First name...'}),
			'last_name': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Last name...'}),
			'date': forms.DateInput(attrs={'class':'form-control ', 'type' :'date', 'placeholder': 'Birthday...'}),
			'username': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Username...'}),
			'email': forms.EmailInput(attrs={'class':'form-control ', 'placeholder': 'Email...'}),
			'phone': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Phone number...'}),
			'studies': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Studies...'}),
			'course': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Course...'}),
			'company': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Company...'}),
			'password1': forms.PasswordInput(attrs={'class':'form-control'}),
			'studentType': forms.Select(choices=studentType_list, attrs={'class':'form-control '}),


        }

		
