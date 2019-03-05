from django import forms
from .models import Persona, InfoComp, Fisico, Foto

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = [ 'registro', 'nombre', 'apellido', 'apellido2', 'apodo', 'domicilio', 'domicilio_laboral', 'fnac', 'dni', 'sexo', 'nacionalidad', 'provincia', 'ciudad', 'lugar_residencia']

class InfoForm(forms.ModelForm):
	class Meta:
		model = InfoComp
		fields = [ 'ocupacion', 'nombre_padre', 'padre_vive', 'nombre_madre', 'madre_vive', 'conyugue', 'conyugue_vive', 'telefono', 'celular', 'estado_civil']

class FisicoForm(forms.ModelForm):
	class Meta:
		model = Fisico
		fields =[ 'altura', 'peso', 'tez', 'ojo_color', 'ojo_forma', 'ojo_tono', 'cabello_color', 'cabello_largo', 'barba_bigote', 'ceja_pilosidad', 'ceja_direccion', 'menton', 'mano_de_uso', 'boca_contorno', 'boca_espesor', 'nariz']


class FotosForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['cara','frente','izquierda','atras','derecha']