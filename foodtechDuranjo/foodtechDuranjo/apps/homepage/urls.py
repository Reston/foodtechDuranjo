from django.conf.urls import patterns, url

urlpatterns = patterns(
	'foodtechDuranjo.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^acerca/$', 'about', name="homepageabout"),
	url(r'^contacto/$', 'contact', name="homapagecontact"),
)
