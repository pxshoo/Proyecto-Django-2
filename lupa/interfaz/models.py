from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class Card(models.Model):
    titulo = models.TextField()
    descripcion = models.TextField(max_length=900)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='img_card', blank=True)
    url = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='cards', default=1)

    def __str__(self):
        return self.titulo
    
class UsuarioManager(BaseUserManager):
    def crear_usuario(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario.')
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico.')
        
        email = self.normalize_email(email)
        usuario = self.model(username=username, email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.crear_usuario(username, email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Grupos',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario. Un usuario obtendrá todos los permisos concedidos a cada uno de sus grupos.',
        related_name="usuario_set",
        related_query_name="usuario",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='Permisos de usuario',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        related_name="usuario_set",
        related_query_name="usuario",
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username