#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
from django import forms


class contactForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su nombre'}))
	empresa = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Razón Social'}))
	SERVICIOS = (('', '------------'), ('reclamos', 'Reclamos',), ('envioLista', 'Envío de lista de precios',), ('visitaRepresentan', 'Visita representante de ventas',),
				('servicio', 'Servicio',), ('otros', 'Otros',))
	referente = forms.ChoiceField(label="Referente a", choices=SERVICIOS, widget=forms.Select(attrs={'class': 'selector'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' nick@email.com'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su Número de teléfono'}))
	texto = forms.CharField(widget=forms.Textarea)

	def clean_asunto(self):
		cd = self.cleaned_data
		asunto = cd.get('asunto')
		if len(asunto) < 3:
			raise forms.ValidationError("El asunto debe tener mas de 2 letras")
		return asunto

	def clean_texto(self):
		cd = self.cleaned_data
		texto = cd.get('texto')
		if len(texto) < 4:
			raise forms.ValidationError("*")
		return texto
