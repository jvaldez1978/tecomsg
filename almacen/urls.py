from django.conf.urls import url

from almacen.views import index_adopcion

urlpatterns = [
	url(r'^index$', index_adopcion),
]