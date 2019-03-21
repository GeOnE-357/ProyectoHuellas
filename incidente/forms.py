from django import forms
from .models import Incidente, TipoIncidente, Parte, Cuerpo, TipoDistintivo
from calzado.models import Calzado
from persona.models import Persona
from huellas.validators import validate_dni, validate_cel, validate_tel, validate_str, validate_date

class IncidenteForm(forms.ModelForm):
	tipo=forms.ModelChoiceField(queryset=TipoIncidente.objects.all(), required=True)
	calzado=forms.ModelChoiceField(queryset=Calzado.objects.all(), required=True)
	persona=forms.ModelChoiceField(queryset=Persona.objects.all(), required=True)
	detalle=forms.CharField(widget=forms.Textarea)
	detalle.widget.attrs.update({'style':'width:98%', 'placeholder':"Escriba un brebe detalle del incidente."})
	class Meta:
		model = Incidente
		fields = ['tipo', 'calzado', 'persona', 'detalle']

class ParteForm(forms.ModelForm):
	OPCIONLADO=(("Izquierda", "Izquierda"),("Derecha", "Derecha"),("Centro","Centro"))
	nombre=forms.ModelChoiceField(queryset=Cuerpo.objects.all(), required=True, validators=[validate_str])
	tipo=forms.ModelChoiceField(queryset=TipoDistintivo.objects.all(), required=True)
	lado=forms.ChoiceField(choices=OPCIONLADO, label="Lado:", widget=forms.Select(),required=True)
	detalle=forms.CharField(widget=forms.Textarea)
	detalle.widget.attrs.update({'style':'width:98%', 'placeholder':"Escriba un brebe detalle de la parte del cuerpo."})
	foto=forms.FileField(required=True)
	class Meta:
		model = Parte
		fields=['nombre','tipo', 'lado', 'detalle', 'foto']

class TipoIncidenteForm(forms.ModelForm):
	nombre=forms.CharField(validators=[validate_str])
	class Meta:
		model=TipoIncidente
		fields=['nombre', 'detalle']

class PeriodoForm(forms.Form):
	inicio=forms.DateField(label="", required=True, validators=[validate_date])
	fin=forms.DateField(label="", required=True, validators=[validate_date])
	inicio.widget.attrs.update({'style':'width:45%', 'placeholder':"Inicio del Periodo: dd/mm/YYYY"})
	fin.widget.attrs.update({'style':'width:45%', 'placeholder':"Fin del Periodo: dd/mm/YYYY"})