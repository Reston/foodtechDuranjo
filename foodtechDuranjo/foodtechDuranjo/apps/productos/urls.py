from django.conf.urls import patterns, url

urlpatterns = patterns(
	'foodtechDuranjo.apps.productos.views',
	url(r'^categoria/$', 'categoria', name="productocategoria"),
	url(r'^producto/(?P<titulo>[-\w]+)/$', 'producto', name="productoproduct"),
	#url(r'^producto/(?P<titulo>[-\w]+)/$', 'producto', name="productoproduct"),
)
