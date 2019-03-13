from django import forms
from .models import Incidente, TipoIncidente, Parte, Cuerpo, ParteFoto, Distintivo, TipoDistintivo
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
	OPCIONLADO=(("Izquierda", "Izquierda"),("Derecha", "Derecha"),("Centro","Centro"))
	cuerpo=forms.ModelChoiceField(queryset=Cuerpo.objects.all(), required=True)
	distintivo=forms.ModelChoiceField(queryset=TipoDistintivo.all(), required=True)
	lado=forms.ChoiceField(choices=OPCIONLADO, label="Lado:", widget=forms.Select(),required=True)
	class Meta:
		fields = ['cuerpo', 'lado', 'distintivo', 'detalle','foto']
