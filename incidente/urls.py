from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.incidenteListar, name="incidente-listar"),
url(r'^Crear/$', views.incidenteCrear, name="incidente-crear"),
url(r'^Crear/Tipo/$', views.incidenteTipo, name="incidente-tipo"),
url(r'^Detalle/(?P<id>\d+)$', views.incidenteDetalle, name="incidente-detalle"),
url(r'^Cuerpo/(?P<id>\d+)$', views.cuerpoCrear, name="incidente-cuerpo"),
url(r'^Estadistica/$', views.incidenteEstadistica, name="incidente-estadistica"),
]