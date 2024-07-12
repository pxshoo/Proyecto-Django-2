from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Card, Usuario
import bcrypt

class CartaCreacionForm(forms.ModelForm):
    titulo = forms.CharField(max_length=90, label='Título')
    descripcion = forms.CharField(max_length=900, label='Descripción')
    precio = forms.IntegerField(label='Precio')
    imagen = forms.ImageField(label='Imagen')
    url = forms.CharField(label='URL')

    class Meta:
        model = Card
        fields = ('titulo', 'descripcion', 'precio', 'imagen', 'url')

class UsuarioCreacionForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Nombre de usuario')
    email = forms.EmailField(max_length=120, label='Correo electrónico')

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.username = self.cleaned_data["username"]
        usuario.email = self.cleaned_data["email"]
        # Encriptar la contraseña usando bcrypt
        hashed_password = bcrypt.hashpw(self.cleaned_data["password1"].encode('utf-8'), bcrypt.gensalt())
        usuario.password = hashed_password.decode('utf-8')
        if commit:
            usuario.save()
        return usuario