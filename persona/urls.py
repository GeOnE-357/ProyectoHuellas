from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.personaListar, name="persona-listar"),
url(r'^Detalle/(?P<id>\d+)$', views.personaDetalle, name="persona-detalle"),
url(r'^Crear/$', views.personaCrear, name="persona-crear"),
url(r'^Crear/Info/(?P<id>\d+)$', views.infoCrear, name="info-crear"),
url(r'^Crear/Fisico/(?P<id>\d+)$', views.fisicoCrear, name="fisico-crear"),
url(r'^Crear/Fotos/(?P<id>\d+)$', views.fotosCrear, name="foto-crear"),
url(r'^Editar/(?P<id>\d+)$', views.personaEditar, name="persona-editar"),
url(r'^Editar/Info/(?P<id>\d+)$', views.infoEditar, name="info-editar"),
url(r'^Editar/Fisico/(?P<id>\d+)$', views.fisicoEditar, name="fisico-editar"),
url(r'^Fotos/(?P<id>\d+)$', views.fotoHistorial, name="foto-historial"),
]