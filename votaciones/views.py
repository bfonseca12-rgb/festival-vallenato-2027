from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Edicion, Opcion, Votacion, VotoRealizado

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'votaciones/register.html', {'form': form})

def home_view(request):
    ediciones = Edicion.objects.filter(activa=True).prefetch_related('categorias__votaciones__opciones')
    
    # Identificar votaciones donde el usuario ya votó
    votaciones_votadas = []
    if request.user.is_authenticated:
        votaciones_votadas = VotoRealizado.objects.filter(
            usuario=request.user
        ).values_list('votacion_id', flat=True)

    return render(request, 'votaciones/index.html', {
        'ediciones': ediciones,
        'votaciones_votadas': votaciones_votadas
    })

@login_required
def votar_view(request, opcion_id):
    if request.method == 'POST':
        opcion = get_object_or_404(Opcion, id=opcion_id)
        votacion = opcion.votacion

        # Verificar si el usuario ya votó
        ya_voto = VotoRealizado.objects.filter(usuario=request.user, votacion=votacion).exists()

        if ya_voto:
            messages.warning(request, "Ya has registrado tu voto único en esta categoría.")
        else:
            opcion.votos += 1
            opcion.save()
            VotoRealizado.objects.create(usuario=request.user, votacion=votacion)
            messages.success(request, f"¡Tu voto por {opcion.nombre_candidato} ha sido registrado con éxito!")

    return redirect('home')