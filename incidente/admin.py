from django.contrib import admin
from .models import Incidente, TipoIncidente, Parte, Cuerpo,TipoDistintivo

admin.site.register(Incidente)
admin.site.register(TipoIncidente)
admin.site.register(Parte)
admin.site.register(Cuerpo)
admin.site.register(TipoDistintivo)