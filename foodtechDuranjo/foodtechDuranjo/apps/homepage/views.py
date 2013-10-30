#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from foodtechDuranjo.apps.homepage.forms import *
from django.template import RequestContext
from django.core.mail import send_mail


def index(request):
	return render_to_response('homepage/index.html', context_instance=RequestContext(request))


def about(request):
	sobrenosotros = "misión de la empresa"
	ctx = {'sobrenosotros': sobrenosotros}
	return render_to_response('homepage/trabajos.html', ctx, context_instance=RequestContext(request))


def products(request):
	return render_to_response('homepage/servicios.html', context_instance=RequestContext(request))


def contact(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s Tipo de servicio: %s Plan: %s' % (cd['nombre'], cd['email'], cd['tipoServicio'], cd['planes'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, cd['email'], ['info@foodtech.com.ve'])
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))
