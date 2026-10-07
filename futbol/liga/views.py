from django.shortcuts import render
from .models import Equipo, Jugador, Partido


def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'liga/equipos.html', {'equipos': equipos})


def jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'liga/jugadores.html', {'jugadores': jugadores})


def partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'liga/partidos.html', {'partidos': partidos})