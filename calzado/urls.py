from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.calzadoListar, name="calzado-listar"),
url(r'^Crear/$', views.calzadoCrear, name="calzado-crear"),
url(r'^Crear/Foto/(?P<id>\d+)$', views.calzadoFoto, name="calzado-foto"),
url(r'^Editar/(?P<id>\d+)$', views.calzadoEditar, name="calzado-editar"),
url(r'^Detalle/(?P<id>\d+)$', views.calzadoDetalle, name="calzado-detalle"),
]