from django.contrib import admin
#from django.contrib.contenttypes import generic
from foodtechDuranjo.apps.productos.models import Categoria, Producto, ImgProductos
from foodtechDuranjo.apps.productos.forms import ProductoForm, CategoriaForm


class CategoriaAdmin(admin.ModelAdmin):
	form = CategoriaForm
	list_display = ('titulo', 'creado_en', 'modificado_en')
	list_display_links = ('titulo',)
	search_fields = ['titulo', 'creado_en', 'modificado_en']


class ImgProductosInline(admin.TabularInline):
	model = ImgProductos


class ProductoAdmin(admin.ModelAdmin):
	form = ProductoForm
	list_display = ('titulo', 'categoria', 'disponible', 'creado_en', 'modificado_en',)
	list_display_links = ('titulo',)
	list_filter = ('disponible', 'categoria')
	search_fields = ['titulo', 'categoria__titulo']
	inlines = [
		ImgProductosInline,
	]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
