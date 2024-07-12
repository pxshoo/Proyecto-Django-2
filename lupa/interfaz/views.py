from functools import wraps
from pyexpat.errors import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def nosotros(request):
    return render(request, 'nosotros.html')

def pagina_prueba(request):
    return render(request, 'pagina_prueba.html')

def prueba(request):
    id_usuario = request.session.get('id_usuario')
    cards = Card.objects.all()
    context = {
        'cards': cards,
        'id_usuario': id_usuario,
    }
    return render(request, 'prueba.html', context)

def crear_carta(request):
    if request.method == 'POST':
        form = CartaCreacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carta creada correctamente.')
            return redirect('prueba')
        else:
            messages.error(request, 'No se ha podido crear la carta. Revisa los errores en el formulario.')
    else:
        form = CartaCreacionForm()
    return render(request, 'cartas/crear_carta.html', {'form': form})

def modificar_carta(request, id):
    carta = get_object_or_404(Card, id=id)
    if request.method == 'POST':
        form = CartaCreacionForm(request.POST, request.FILES, instance=carta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carta modificado correctamente.')
            return redirect('prueba')
        else:
            messages.error(request, "No se ha podido modificar la carta.")
    else:
        form = CartaCreacionForm(instance=carta)
    context = {
        'form': form,
        'mensaje_correcto': messages.get_messages(request),
        'mensaje_incorrecto': messages.get_messages(request),
    }
    return render(request, 'cartas/modificar_carta.html', context)

def mantener_sesion(usuario):
    def decorator(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            session_key = f'{usuario}'
            if request.session.get(session_key, False):
                return function(request, *args, **kwargs)
        return wrap
    return decorator

def cerrar_sesion(request):
    session_key = 'usuario'
    request.session.pop(session_key, None)
    request.session.flush()
    return redirect('prueba')

def eliminar_carta(request, id):
    carta = get_object_or_404(Card, id=id)
    carta.delete()
    messages.success(request, 'Carta eliminada correctamente.')
    return redirect('prueba')

def register(request):
    if request.method == 'POST':
        form = UsuarioCreacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': form.errors})
    else:
        form = UsuarioCreacionForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                usuario = Usuario.objects.get(username=username)
                if bcrypt.checkpw(password.encode('utf-8'), usuario.password.encode('utf-8')):
                    if usuario.is_active:
                        request.session['usuario'] = True
                        request.session['id_usuario'] = usuario.id
                        return redirect('prueba')
                    else:
                        messages.error(request, 'Su usuario no se encuentra activo.')
                else:
                    messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            except Usuario.DoesNotExist:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Debes ingresar tanto el nombre de usuario como la contraseña.')
        return render(request, 'login.html', {'form': None})
    else:
        return render(request, 'login.html', {'form': None})