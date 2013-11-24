#-*- encoding: utf-8 -*-
from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from foodtechDuranjo.apps.productos.models import Categoria


class StaticViewSitemap(sitemaps.Sitemap):
	priority = 1
	changefreq = 'yearly'

	def items(self):
		return [
				'homepageindex',
				"homepageabout",
				"homapagecontact",
				]

	def location(self, item):
		return reverse(item)


class CategoriaSitemap(sitemaps.Sitemap):
	changefreq = 'monthly'
	priority = 0.5

	def items(self):
		return Categoria.objects.all()

	def lastmod(self, obj):
		return obj.modificado_en
