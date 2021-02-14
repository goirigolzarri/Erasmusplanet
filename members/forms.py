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
	username = forms.CharField(label="Username", max_length=30,
		widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'type' :'text', 'id' : 'username', 'size' : '10px','placeholder': 'Username...'}))

	email = forms.EmailField(label="Email",
		widget=forms.EmailInput(attrs={'class': 'mdl-emailfield__input', 'type' :'text', 'id' : 'email', 'placeholder': 'Email...'}))

	first_name = forms.CharField(label='Name', max_length=30,
		widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'size': '23', 'type' :'text', 'id' : 'first_name', 'placeholder': 'Name...'}))
	
	last_name = forms.CharField(label='Last name', max_length=30,
		widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'size': '23', 'type' :'text', 'id' : 'last_name', 'placeholder': 'Last name...'}))

	#gender = forms.ChoiceField(
	#	widget=forms.Select(attrs={'class': 'form-control', 'size': '7'}))
	
	date = forms.DateField(label='Birthday',
		widget=forms.DateInput(attrs={'class': 'mdl-datefield__input', 'size': '40', 'type' :'date', 'id' : 'date', 'placeholder': 'Birthday...'}))
	
	phone = forms.CharField(label="Phone", max_length=30,
		widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'type' :'text', 'id' : 'phone', 'placeholder': 'Phone...'}))
	
	#gender = forms.ChoiceField(
	#	widget=forms.Select(attrs={'class': 'mdl-choicefield__input', 'size': '40'}))
	
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
		fields = ['username', 'first_name', 'last_name', 'date' , 'gender' ,'country', 'phone_prefix', 'phone', 'studentType', 'cityOrigin1',
		 'cityDestination1', 'cityDestination2', 'cityDestination3', 'universityOrigin', 'universityDestination', 'studies', 'email', 'password1', 'password2', 'course', 'company']

