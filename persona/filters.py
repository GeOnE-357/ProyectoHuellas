from .models import Persona
import django_filters

class PersonaFilter(django_filters.FilterSet):
    nombre=django_filters.CharFilter(label=False,)
    apellido=django_filters.CharFilter(label=False,)
    dni=django_filters.NumberFilter(label=False,)
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'dni']