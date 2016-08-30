from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader

from .models import Tournament
from .models import User

# Create your views here.

def index (request):
    tournaments = Tournament.objects.all()
    context = {'tournaments': tournaments}
    return render(request, 'tenis/index.html', context)


def tournament (request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    progress = int(100 * tournament.participants_registered / tournament.participants_max)
    context = {'tournament': tournament, 'progress': progress}
    return render(request, 'tenis/tournament.html', context)
