#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from foodtechDuranjo.apps.homepage.forms import *
from django.template import RequestContext
from django.core.mail import send_mail
from blogango.models import BlogEntry


def index(request):
	entradas = BlogEntry.objects.order_by('-created_on')
	entradas= entradas[:2]
	ctx = {'entradas':entradas}
	return render_to_response('homepage/index.html',ctx, context_instance=RequestContext(request))


def about(request):
	sobrenosotros = "misión de la empresa"
	ctx = {'sobrenosotros': sobrenosotros}
	return render_to_response('homepage/quienesomos.html', ctx, context_instance=RequestContext(request))


def products(request):
	return render_to_response('homepage/producto.html', context_instance=RequestContext(request))


def contact(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s Empresa: %s' % (cd['nombre'], cd['empresa'], cd['email'])
			content = u'Empresa: %s Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['empresa'], cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, 'info@foodtech.com.ve', ['info@foodtech.com.ve']) #falta enviar a los demás correos que dijeron
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))
