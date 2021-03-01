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
	body = RichTextField(blank=True)

	def __str__(self):

		return self.title