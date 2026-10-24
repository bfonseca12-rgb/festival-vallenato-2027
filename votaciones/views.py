from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.management import call_command
from .models import Candidato, Voto

def home(request):
    # Ejecuta automáticamente las migraciones faltantes si la tabla no existe
    try:
        call_command('migrate', interactive=False)
    except Exception:
        pass

    # Crea/actualiza automáticamente el superusuario administrador
    user, created = User.objects.get_or_create(username='admin')
    user.set_password('admin1234')
    user.is_staff = True
    user.is_superuser = True
    user.save()

    candidatos = Candidato.objects.all()
    total_votos = Voto.objects.count()
    
    ha_votado = False
    if request.user.is_authenticated:
        ha_votado = Voto.objects.filter(usuario=request.user).exists()

    context = {
        'candidatos': candidatos,
        'total_votos': total_votos,
        'ha_votado': ha_votado,
    }
    return render(request, 'votaciones/index.html', context)

home_view = home


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Ya puedes votar.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def votar(request, candidato_id):
    if Voto.objects.filter(usuario=request.user).exists():
        messages.error(request, 'Ya has registrado tu voto anteriormente.')
        return redirect('home')
    
    candidato = get_object_or_404(Candidato, id=candidato_id)
    Voto.objects.create(usuario=request.user, candidato=candidato)
    messages.success(request, f'¡Tu voto por {candidato.nombre} ha sido registrado!')
    return redirect('home')