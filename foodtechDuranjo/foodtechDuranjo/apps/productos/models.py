# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse


class Categoria(models.Model):
	titulo = models.CharField(max_length=20, help_text='Hasta 20 caracteres y solamente alfanuméricos', unique=True)
	#descripcion = models.CharField(max_length=30, help_text='Hasta 30 caracteres')
	imagen = models.ImageField(upload_to='imgcategorias')
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('productoproduct', kwargs={'titulo': titulo})


class Producto(models.Model):
	titulo = models.CharField(max_length=25, help_text='Hasta 25 caracteres y solamente alfanuméricos')
	descripcion = models.TextField()
	categoria = models.ForeignKey(Categoria)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	disponible = models.BooleanField(default=True, help_text='Disponibilidad del producto')
	imagen_abajo = models.ImageField(upload_to='imgproductos')

	def __unicode__(self):
		return self.titulo

	#def get_absolute_url(self):
	#	titulo = self.titulo.replace(' ', '_')
	#	return reverse('productoproducto', kwargs={'titulo': titulo})


class ImgProductos(models.Model):
	producto = models.ForeignKey(Producto, related_name='imagenes')
	imagen = models.ImageField(upload_to='imgproductos')
	titulo = models.CharField(max_length=30, help_text='Hasta 30 caracteres y solamente alfanuméricos')

