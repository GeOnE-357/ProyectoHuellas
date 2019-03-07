from django.contrib import admin
from .models import Calzado, FotoCalzado, Marca, Forma 
# Register your models here.
admin.site.register(Calzado)
admin.site.register(Marca)
admin.site.register(Forma)
admin.site.register(FotoCalzado)