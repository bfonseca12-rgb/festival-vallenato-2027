from django.db import models
from django.contrib.auth.models import User

class Edicion(models.Model):
    nombre = models.CharField(max_length=100)
    anio = models.IntegerField()
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.anio})"

class Categoria(models.Model):
    edicion = models.ForeignKey(Edicion, on_delete=models.CASCADE, related_name='categorias')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.edicion.anio}"

class Votacion(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='votaciones')
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Opcion(models.Model):
    votacion = models.ForeignKey(Votacion, on_delete=models.CASCADE, related_name='opciones')
    nombre_candidato = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    foto_url = models.URLField(max_length=500, blank=True, help_text="Enlace a la imagen del cantante")
    audio_url = models.URLField(max_length=500, blank=True, help_text="Enlace al archivo de audio MP3 de muestra")
    votos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre_candidato

class VotoRealizado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    votacion = models.ForeignKey(Votacion, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'votacion') # Garantiza un solo voto por usuario en cada votación