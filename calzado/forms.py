from django import forms
from .models import Calzado, FotoCalzado, Marca, Forma
from huellas.validators import validate_dni, validate_cel, validate_tel, validate_str

class CalzadoForm(forms.ModelForm):
	forma_sup=forms.ModelChoiceField(queryset=Forma.objects.all(), required=True)
	forma_inf=forms.ModelChoiceField(queryset=Forma.objects.all(), required=True)
	marca=forms.ModelChoiceField(queryset=Marca.objects.all(), required=True)
	class Meta:
		model=Calzado
		fields=['forma_sup', 'forma_inf', 'marca']

class FotoCalzadoForm(forms.ModelForm):
	class Meta:
		model=FotoCalzado
		fields=['frente','izquierda','atras','derecha','inferior']

class FormaForm(forms.ModelForm):
	nombre=forms.CharField(required=True, validators=[validate_str])
	class Meta:
		model=Forma
		fields=['nombre', 'motivo']

class MarcaForm(forms.ModelForm):
	class Meta:
		model=Marca
		fields=['nombre']