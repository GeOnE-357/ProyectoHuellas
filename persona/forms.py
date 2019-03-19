from django import forms
from .models import Persona, InfoComp, Fisico, Foto
from huellas.validators import validate_dni, validate_cel, validate_tel, validate_str, validate_dir

class PersonaForm(forms.ModelForm):
    dni=forms.IntegerField(validators=[validate_dni])
    nombre=forms.CharField(validators=[validate_str])
    apellido=forms.CharField(validators=[validate_str])
    nacionalidad=forms.CharField(validators=[validate_str])
    provincia=forms.CharField(validators=[validate_str])
    ciudad=forms.CharField(validators=[validate_str])
    lugar_residencia=forms.CharField(validators=[validate_str])
    domicilio=forms.CharField(validators=[validate_dir])
    domicilio_laboral=forms.CharField(validators=[validate_dir])
    class Meta:
        model = Persona
        fields = [ 'registro', 'nombre', 'apellido', 'apellido2', 'apodo', 'domicilio', 'domicilio_laboral', 'fnac', 'dni', 'sexo', 'nacionalidad', 'provincia', 'ciudad', 'lugar_residencia']

class InfoForm(forms.ModelForm):
    celular=forms.IntegerField(validators=[validate_cel])
    telefono=forms.IntegerField(validators=[validate_tel])
    nombre_padre=forms.CharField(validators=[validate_str])
    nombre_madre=forms.CharField(validators=[validate_str])
    conyugue=forms.CharField(validators=[validate_str])
    ocupacion=forms.CharField(validators=[validate_str])
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