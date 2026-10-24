from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Voto

# Importa el modelo de participante/candidato según como esté definido en models.py
try:
    from .models import Candidato as ModeloCandidato
except ImportError:
    from .models import Participante as ModeloCandidato


def home(request):
    # Si no hay registros en la base de datos, los crea automáticamente
    if not ModeloCandidato.objects.exists():
        ModeloCandidato.objects.create(
            nombre="Silvestre Dangond",
            categoria="Rey Vallenato",
            descripcion="Exponente del vallenato moderno con gran trayectoria."
        )
        ModeloCandidato.objects.create(
            nombre="Rolando Ochoa",
            categoria="Mejor Acordeonero",
            descripcion="Aclamado acordeonero y compositor tradicional."
        )
        ModeloCandidato.objects.create(
            nombre="Elder Dayán Díaz",
            categoria="Rey Vallenato",
            descripcion="Representante de la nueva ola vallenata."
        )

    candidatos = ModeloCandidato.objects.all()
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
    
    candidato = get_object_or_404(ModeloCandidato, id=candidato_id)
    
    # Intenta guardar el voto adaptándose al nombre de la clave foránea en Voto
    voto = Voto(usuario=request.user)
    if hasattr(voto, 'candidato'):
        voto.candidato = candidato
    elif hasattr(voto, 'participante'):
        voto.participante = candidato
    voto.save()

    messages.success(request, f'¡Tu voto por {candidato.nombre} ha sido registrado!')
    return redirect('home')