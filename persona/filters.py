from .models import Persona
from django.forms.widgets import TextInput
import django_filters

class PersonaFilter(django_filters.FilterSet):
    nombre=django_filters.CharFilter(label=False, widget=TextInput(attrs={'placeholder': 'Nombre...'}))
    apellido=django_filters.CharFilter(label=False, widget=TextInput(attrs={'placeholder': 'Apellido...'}))
    dni=django_filters.NumberFilter(label=False, widget=TextInput(attrs={'placeholder': 'Dni...'}))
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'dni']