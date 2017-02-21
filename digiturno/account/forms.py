from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario
from django.contrib.auth.models import User


class IdentificacionForm(forms.Form):
    cedula = forms.CharField(max_length=20)

class InfoUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['cedula']

class InfoUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

ROLES = (
('recepcion', 'Recepcion'),
('atencion', 'Atencion'),
('admin', 'Administrativo'),
('usuario', 'Usuario'),
)

class RegistroForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    cedula = forms.CharField(max_length=20)
    correo = forms.EmailField()

