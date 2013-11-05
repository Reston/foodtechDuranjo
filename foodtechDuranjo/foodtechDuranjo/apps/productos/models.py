# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse


class Categoria(models.Model):
	titulo = models.CharField(max_length=20, help_text='Hasta 20 caracteres y solamente alfanuméricos', unique=True)
	imagen = models.ImageField(upload_to='imgcategorias')
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('categoria', kwargs={'titulo': titulo})


class Producto(models.Model):
	titulo = models.CharField(max_length=25, help_text='Hasta 25 caracteres y solamente alfanuméricos')
	descripcion_corta = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	categoria = models.ForeignKey(Categoria)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	disponible = models.BooleanField(default=True, help_text='Disponibilidad del producto')
	destacado = models.BooleanField(default=False, help_text='Promocionar producto en sección de destacados')

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('productoproducto', kwargs={'titulo': titulo})


class ImgProductos(models.Model):
	producto = models.ForeignKey(Producto, related_name='imagenes')
	imagen = models.ImageField(upload_to='imgproductos')

