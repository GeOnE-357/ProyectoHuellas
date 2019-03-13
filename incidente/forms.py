from django import forms
from .models import Incidente, TipoIncidente, Parte, ParteLista, ParteFoto, Distintivo, Tipo
from calzado.models import Calzado
from persona.models import Persona

class IncidenteForm(forms.ModelForm):
	tipo=forms.ModelChoiceField(queryset=TipoIncidente.objects.all(), required=True)
	calzado=forms.ModelChoiceField(queryset=Calzado.objects.all(), required=True)
	persona=forms.ModelChoiceField(queryset=Persona.objects.all(), required=True)
	detalle=forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Incidente
		fields = ['tipo', 'calzado', 'persona', 'detalle']

class ParteFrom(forms.ModelForm):
	class Meta:
		fields = ['nombre', 'lado', 'tipo', 'detalle','foto']
