from django.contrib import admin
from .models import Candidato, Voto

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'descripcion')

@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'candidato', 'fecha')