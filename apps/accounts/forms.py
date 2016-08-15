# accounts/forms.py

from django import forms
from django.contrib.auth.models import User


class RegistroUserForm(forms.Form):

    username = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre de Usuario',}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Correo Electronico'}))
    password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'}))
    password2 = forms.CharField(    min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirma tu Contraseña'}))
    photo = forms.ImageField(required=False)

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Este E-mail ya esta registrado.')
        return email

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2

class EditarEmailForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        """Obtener request"""
        self.request = kwargs.pop('request')
        return super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        # Comprobar si ha cambiado el email
        actual_email = self.request.user.email
        username = self.request.user.username
        if email != actual_email:
            # Si lo ha cambiado, comprobar que no exista en la db.
            # Exluye el usuario actual.
            existe = User.objects.filter(email=email).exclude(username=username)
            if existe:
                raise forms.ValidationError('Este E-mail ya esta registrado.')
        return email


class EditarContrasenaForm(forms.Form):

    actual_password = forms.CharField(
        label='Contraseña actual',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password = forms.CharField(
        label='Nueva contraseña',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(
        label='Repetir contraseña',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, user, data=None):
        self.user = user
        super(EditarContrasenaForm, self).__init__(data=data)

    def clean_password(self):
        password_old = self.cleaned_data.get('actual_password', None)
        if not self.user.check_password(password_old):
            raise ValidationError('Invalid password')
    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2