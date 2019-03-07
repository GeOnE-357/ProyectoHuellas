from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.calzadoListar, name="calzado-listar"), 
]