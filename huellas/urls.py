from django.conf.urls import include, url #importe las librerias include y url.
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$', views.home, name="home"),
]
