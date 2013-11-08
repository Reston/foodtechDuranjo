#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from foodtechDuranjo.apps.productos.models import Categoria, Producto, ImgProductos
from django.shortcuts import get_object_or_404


def producto(request, titulo):
	titulo = titulo.replace('_', ' ')
	categoria = get_object_or_404(Categoria, titulo=titulo)
	productos = Producto.objects.filter(categoria_id=categoria.pk)
	imagenes = ImgProductos.objects.filter(producto__in=list(productos))
	ctx = {'producto': productos, 'imagenes': imagenes}
	return render_to_response('productos/producto.html', ctx, context_instance=RequestContext(request))


def categoria(request):
	mensaje = ''
	lista_categorias = Categoria.objects.all()
	ctx = {
		'lista_categorias': lista_categorias,
		'mensaje': mensaje
	}
	return render_to_response('productos/categoria.html', ctx, context_instance=RequestContext(request))
