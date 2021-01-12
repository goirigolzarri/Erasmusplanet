from django.contrib.auth.forms import UserCreationForm

from members.models import User
from django import forms

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
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username...'}))
	email =forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surnames...'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Birthdate...'}))
	#password1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password...'}))
	#password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Repeat password...'}))
	phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone...'}))
	#gender = forms.CharField(widget=forms.Select(attrs={'size': '8'}))
	#country_prefix = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country...'}))
	studies = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estudies...'}))
	cityOrigin1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City origin...'}))
	#cityDestination1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First option city...'}))
	cityDestination2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Second option city...'}))
	cityDestination3 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Third option city...'}))
	universityOrigin = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'University origin...'}))
	course = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course...'}))
	company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company...'}))

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'date' , 'gender' ,'country', 'phone_prefix', 'phone', 'studentType', 'cityOrigin1', 'cityDestination1', 'cityDestination2', 'cityDestination3', 'universityOrigin', 'universityDestination', 'studies', 'email', 'password1', 'password2', 'course', 'company']