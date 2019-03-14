from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.incidenteListar, name="incidente-listar"),
url(r'^Crear/$', views.incidenteCrear, name="incidente-crear"),
url(r'^Detalle/(?P<id>\d+)$', views.incidenteDetalle, name="incidente-detalle"),
]