from django.conf.urls import patterns, url

urlpatterns = patterns(
	'foodtechDuranjo.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^trabajos/$', 'about', name="homepageabout"),
	url(r'^servicios/$', 'products', name="homepageproduct"),
	url(r'^contacto/$', 'contact', name="homapagecontact"),
)