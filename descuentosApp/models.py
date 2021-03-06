from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.


class Country(models.Model):

	name = models.CharField(max_length=30)

	class Meta:
        
		ordering = ['name']



	def __str__(self):

		return self.name



class Province(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)



	def __str__(self):

		return self.name


class City(models.Model):
	province = models.ForeignKey(Province, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)


	def __str__(self):

		return self.name

	def get_absolute_url(self):
		return reverse('City')



class University(models.Model):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)



	def __str__(self):

		return self.name



class Guide(models.Model):

	city = models.ForeignKey(City, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, default='')
	informacion_general = RichTextField(blank=True)
	como_llegar = RichTextField(blank=True)
	alojamiento = RichTextField(blank=True)
	ocio = RichTextField(blank=True)
	divisas = RichTextField(blank=True)
	banco_sim = RichTextField(blank=True)
	donde_comprar = RichTextField(blank=True)

	def __str__(self):

		return self.title