from django.db import models

# Create your models here.
class Unidad(models.Model):
	descripcion = models.CharField(max_length = 50)

	def __str__(self):
		return '{}'.format(self.descripcion)

	class Meta:
	    verbose_name_plural = "Unidades"


class Material(models.Model):
	unidad = models.ForeignKey(Unidad, null=False, blank=False)	
	codigo = models.CharField(max_length = 50)
	descripcion = models.CharField(max_length = 250)
	stock = models.IntegerField()
	stockminimo = models.IntegerField()	

	def __str__(self):
		return '{} {} {}'.format(self.codigo, self.descripcion, self.stock)

	class Meta:
	    verbose_name_plural = "Materiales"


class Empresa(models.Model):
	descripcion = models.CharField(max_length = 50)
	
	def __str__(self):
		return '{}'.format(self.descripcion)		

	class Meta:
	    verbose_name_plural = "Empresas"


class Persona(models.Model):
	empresa = models.ForeignKey(Empresa, null=False, blank=False)	
	documento = models.CharField(max_length = 15)
	apellidos = models.CharField(max_length = 50)
	nombres = models.CharField(max_length = 50)
	correo = models.EmailField()

	def __str__(self):
		return '{} {}'.format(self.apellidos, self.nombres, self.correo)				

	class Meta:
	    verbose_name_plural = "Personas"

class Salida(models.Model):
	material = models.ForeignKey(Material, null=False, blank=False)	
	persona = models.ForeignKey(Persona, null=False, blank=False)	
	fecha = models.DateTimeField()
	cantidad = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.material.codigo)				

