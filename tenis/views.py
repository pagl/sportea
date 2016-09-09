from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader
from django import forms
from django.shortcuts import redirect
import datetime
from .models import Tournament, Match, Registration
from django.contrib.auth.models import User
import math
from django.db.models import Q

# Create your views here.

def index (request):
    tournaments_per_page = 10
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
    tournaments_per_page = 10
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
    user = request.user
    registered = Registration.objects.filter(Q(player=user) & Q(tournament=tournament)).count()
    print registered
    progress = int(100 * tournament.participants_registered / tournament.participants_max)
    context = {'tournament': tournament, 'progress': progress, 'registered': registered}
    return render(request, 'tenis/tournament.html', context)


def new_tournament (request):
    return render(request, 'tenis/new.html')


def edit (request, edit_id):
    tournament = Tournament.objects.get(id=edit_id)
    context = {'tournament': tournament}
    return render(request, 'tenis/edit.html', context)


def join_tournament (request, join_id):
    tournament = Tournament.objects.get(id=join_id)
    user = request.user
    context = {'tournament': tournament,
               'user': user}
    return render(request, 'tenis/join.html', context)


def register_to_tournament (request, register_id):
    player = request.user
    tournament = Tournament.objects.get(id=register_id)
    if request.method == 'POST':
        license = request.POST.get('license', '')
        rank = request.POST.get('rank', '')

        registration = Registration(player = player,
                                    tournament = tournament,
                                    license = license,
                                    ranking = rank)
        registration.save()

    return redirect('tenis.views.tournament', tournament.id)

def update_tournament (request, update_id):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        organizer = request.user
        date = datetime.datetime.strptime(request.POST.get('date', ''), "%m/%d/%Y %I:%M %p").strftime("%Y-%m-%d %H:%M")
        deadline = datetime.datetime.strptime(request.POST.get('deadline', ''), "%m/%d/%Y %I:%M %p").strftime("%Y-%m-%d %H:%M")
        address = request.POST.get('address', '')
        participants_max = request.POST.get('participants', '')
        logo = request.FILES['logo']

        today = datetime.datetime.now()
        if (date < today.strftime("%Y-%m-%d %H:%M")
        or  deadline > date):
            return redirect('tenis.views.new_tournament')


        tournament = Tournament.objects.get(id = update_id)
        tournament.name = name
        tournament.datetime = date
        tournament.deadline = deadline
        tournament.address = address
        tournament.participants_max = participants_max
        tournament.logo = logo

        tournament.save()

    return redirect('tenis.views.tournament', tournament.id)


def add_tournament (request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        organizer = request.user
        date = datetime.datetime.strptime(request.POST.get('date', ''), "%m/%d/%Y %I:%M %p").strftime("%Y-%m-%d %H:%M")
        deadline = datetime.datetime.strptime(request.POST.get('deadline', ''), "%m/%d/%Y %I:%M %p").strftime("%Y-%m-%d %H:%M")
        address = request.POST.get('address', '')
        participants_max = request.POST.get('participants', '')
        logo = request.FILES['logo']

        today = datetime.datetime.now()
        if (date < today.strftime("%Y-%m-%d %H:%M")
        or  deadline > date):
            return redirect('tenis.views.new_tournament')

        newTournament = Tournament(name = name,
                                   organizer = organizer,
                                   datetime = date,
                                   deadline = deadline,
                                   address = address,
                                   participants_max = participants_max,
                                   participants_registered = 0,
                                   logo = logo)
        newTournament.save()
        tournament_id = newTournament.id

    return redirect('tenis.views.tournament', tournament_id)


def mytournaments (request):
    tournaments = Tournament.objects.all().order_by('datetime').filter(organizer=request.user)
    context = {
        'tournaments': tournaments,
    }
    return render(request, 'tenis/mytournaments.html', context)


def mymatches (request):
    matches = Match.objects.all().filter(Q(player1=request.user) | Q(player2=request.user))
    opponents = [match.player1 if match.player1 != request.user else match.player2 for match in matches]
    print opponents
    context = {
        'matches': matches,
        'opponents': opponents,
    }
    return render(request, 'tenis/mymatches.html', context)
