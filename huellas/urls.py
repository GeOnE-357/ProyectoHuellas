from django.conf.urls import include, url #importe las librerias include y url.
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$', views.home, name="home"),
    url(r'^Persona/', include('persona.urls')),
    url(r'^Calzado/', include('calzado.urls')),
    url(r'^Incidente/', include('incidente.urls')),
    url(r'^Control/', include('control.urls')),
    url(r'^Usuario/Login/$', views.loginUsuario, name="login"),
    url(r'^Usuario/Logout/$', views.logoutUsuario, name="logout"),
    url(r'^Usuario/Password/$', views.passwordUsuario, name="usuario-password"),
    url(r'^(?P<tipo>\w+)/Registrar/$', views.registrarUsuario, name="usuario-registrar"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)