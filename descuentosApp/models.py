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
	imagen_informacion_general = models.ImageField(null=True, blank=True, upload_to="images/")
	informacion_general = RichTextField(blank=True)
	como_llegar = RichTextField(blank=True)
	comida = RichTextField(blank=True, default = '')
	alojamiento = RichTextField(blank=True)
	ocio = RichTextField(blank=True)
	divisas = RichTextField(blank=True)
	banco_sim = RichTextField(blank=True)
	donde_comprar = RichTextField(blank=True)

	def __str__(self):

		return self.title



class CategoriaProducto(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Producto(models.Model):
	nombre = models.CharField(max_length=30, null=False, blank=False, default='Producto Erasmus Planet')
	codigo = models.CharField(max_length=10, null=False, blank=False)
	precio = models.IntegerField(default=10)
	detalles = models.CharField(max_length=50, null=True)
	bandera = models.CharField(max_length=20)
	TALLA_CHOICES = (('1', 'S'), ('2', 'M'), ('3', 'L'), ('4', 'XL'))
	talla = models.CharField(max_length=10, choices=TALLA_CHOICES, null=True, default='')
	COLORES_CHOICES = (('1', 'Rojo'), ('2', 'Blanco'), ('3', 'Negro'), ('4', 'Azul'))
	color = models.CharField(max_length=10, choices=COLORES_CHOICES, null=True, default='') 

