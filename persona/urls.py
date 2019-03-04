from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.personaListar, name="persona-listar"),
url(r'^Crear/$', views.personaCrear, name="persona-crear"),
url(r'^Crear/InfoComp/(?P<id>\d+)$', views.infoCrear, name="info-crear"),
url(r'^Crear/Fisico/(?P<id>\d+)$', views.fisicoCrear, name="fisico-crear")
]