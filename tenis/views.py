from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader

from .models import Tournament
from django.contrib.auth.models import User
import math
from django.db.models import Q

# Create your views here.

def index (request):
    tournaments_per_page = 7
    tournaments = Tournament.objects.all().order_by('datetime')
    pages = range(0, int(math.ceil(float(len(tournaments)) / tournaments_per_page)))

    current_page = 1
    tournamentRangeStart = (current_page - 1)  * tournaments_per_page
    tournamentRangeEnd = tournamentRangeStart + tournaments_per_page
    tournaments = tournaments[tournamentRangeStart : tournamentRangeEnd]
    context = {
        'tournaments': tournaments,
        'pages': pages,
        'current_page': current_page,
    }
    return render(request, 'tenis/index.html', context)


def tournaments_list (request, current_page):
    tournaments_per_page = 7
    tournaments = Tournament.objects.all().order_by('datetime')
    pages = range(0, int(math.ceil(float(len(tournaments)) / tournaments_per_page)))

    tournamentRangeStart = (int(current_page) - 1)  * tournaments_per_page
    tournamentRangeEnd = tournamentRangeStart + tournaments_per_page
    tournaments = tournaments[tournamentRangeStart : tournamentRangeEnd]
    context = {
        'tournaments': tournaments,
        'pages': pages,
        'current_page': int(current_page),
    }
    return render(request, 'tenis/index.html', context)


def tournaments_list_with_search (request, search_for):
    tournaments = Tournament.objects.filter(Q(title__icontains=search_for) | Q(intro__icontains=search_for) | Q(content__icontains=search_for)).order_by('datetime')
    tournaments = Tournament.objects.all().order_by('datetime')

    context = {
        'tournaments': tournaments,
        'pages': 1,
        'current_page': 1,
    }
    return render(request, 'tenis/index.html', context)


def tournament (request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    progress = int(100 * tournament.participants_registered / tournament.participants_max)
    context = {'tournament': tournament, 'progress': progress}
    return render(request, 'tenis/tournament.html', context)
