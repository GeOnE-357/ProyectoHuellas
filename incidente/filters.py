from .models import Incidente, TipoIncidente, Parte, Cuerpo, TipoDistintivo
from persona.models import Persona
from calzado.models import Calzado
import django_filters

class IncidenteFilter(django_filters.FilterSet):
	tipo=django_filters.ModelChoiceFilter(queryset=TipoIncidente.objects.all(), label=False, empty_label="Tipo de incidente")
	calzado=django_filters.ModelChoiceFilter(queryset=Calzado.objects.all(), label=False, empty_label="Calzado")
	persona=django_filters.ModelChoiceFilter(queryset=Persona.objects.all(), label=False,empty_label="Persona")
	class Meta:
		model = Incidente
		fields = ['tipo', 'calzado', 'persona']