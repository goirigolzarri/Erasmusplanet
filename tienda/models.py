from django.db import models
from django.urls import reverse

# Create your models here.

class CategoriaProducto(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class ColorProducto(models.Model):
	name = models.CharField(max_length=15)
	
	def __str__(self):
		return self.name





	
class Producto(models.Model):

	name = models.CharField(max_length=30, null=False, blank=False, default='Producto Erasmus Planet')
	codigo = models.CharField(max_length=10, null=False, blank=False)
	precio = models.IntegerField(default=10)
	detalles = models.CharField(max_length=50, null=True)
	bandera = models.CharField(max_length=20)
	TALLA_CHOICES = (('1', 'XS'), ('2', 'S'), ('3', 'M'), ('4', 'L'), ('5', 'XL'), ('6', 'XXL'))
	talla = models.CharField(max_length=10, choices=TALLA_CHOICES, null=True, default='')
	bandera = models.CharField(null=True, max_length=30)
	fecha = models.CharField(null= True, max_length=20)
	color = models.ForeignKey(ColorProducto, on_delete=models.CASCADE, default='') 

	def get_absolute_url(self):
		return reverse('Tienda')

	def __str__(self):
		return self.name


