from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .validators import validate_dni, validate_str, validate_pos

class UsuarioForm(UserCreationForm):
	username = forms.IntegerField(required=True, label='Nombre de Usuario (DNI):', validators=[validate_dni, validate_pos])
	first_name = forms.CharField(max_length=30, required=False, label='Nombre:', validators=[validate_str])
	last_name = forms.CharField(max_length=30, required=False, label='Apellido:', validators=[validate_str])
	email = forms.EmailField(max_length=254)
	password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña:")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Contraseña (confirmación):")
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2', )