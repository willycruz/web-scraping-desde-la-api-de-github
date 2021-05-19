from django import forms
from repositorios.models import Usuario


class UserForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = '__all__'

		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control'}),
		}