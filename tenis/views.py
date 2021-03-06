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
from django.http import Http404


def index (request):
    today = datetime.datetime.today()
    tournaments_per_page = 10
    tournaments = Tournament.objects.filter(deadline__gte=today).order_by('datetime')
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
    today = datetime.datetime.today()
    tournaments_per_page = 10
    tournaments = Tournament.objects.filter(deadline__gte=today).order_by('datetime')
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


def tournament (request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    user = request.user
    if (request.user.is_authenticated()):
        registered = Registration.objects.filter(Q(player=user) & Q(tournament=tournament)).count()
    else:
        registered = 0

    today = datetime.datetime.now()
    diff = (tournament.deadline.replace(tzinfo=None) - today)
    days = diff.days
    hours = int(diff.seconds / 3600)
    minutes = int((diff.seconds / 60) % 60)
    seconds = int(diff.seconds % 60)
    progress = int(100 * tournament.participants_registered / tournament.participants_max)

    ladder = []
    if tournament.stage != 0:
        for stage in range(1, tournament.stage):
            ladder.append(Match.objects.filter(Q(tournament=tournament)
                                         & Q(stage=stage)))


    context = {
               'tournament': tournament,
               'progress': progress,
               'registered': registered,
               'days': days,
               'hours': hours,
               'minutes': minutes,
               'seconds': seconds,
               'ladder': ladder,
              }
    return render(request, 'tenis/tournament.html', context)


def new_tournament (request):
    if (not request.user.is_authenticated()):
        raise Http404("Access Denied")
    return render(request, 'tenis/new.html')


def edit (request, edit_id):
    if (not request.user.is_authenticated()):
        raise Http404("Access Denied")
    tournament = Tournament.objects.get(id=edit_id)
    context = {'tournament': tournament}
    return render(request, 'tenis/edit.html', context)


def join_tournament (request, join_id):
    if (not request.user.is_authenticated()):
        raise Http404("Access Denied")
    tournament = Tournament.objects.get(id=join_id)
    user = request.user
    context = {'tournament': tournament,
               'user': user}
    return render(request, 'tenis/join.html', context)


def register_to_tournament (request, register_id):
    if (not request.user.is_authenticated()):
        raise Http404("Access Denied")
    player = request.user
    tournament = Tournament.objects.get(id=register_id)
    if request.method == 'POST':
        license = request.POST.get('license', '')
        rank = request.POST.get('rank', '')
        valid = Registration.objects.filter(Q(tournament=tournament) & (Q(ranking=rank) | Q(license=license))).count() == 0

        if (valid):
            registration = Registration(player = player,
                                        tournament = tournament,
                                        license = license,
                                        ranking = rank)
            if (tournament.participants_registered < tournament.participants_max):
                tournament.participants_registered += 1
                tournament.save()
                registration.save()

    return redirect('tenis.views.tournament', tournament.id)


def update_tournament (request, update_id):
    if (not request.user.is_authenticated()):
        raise Http404("Access Denied")
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
    if (not request.user.is_authenticated()):
        raise Http404("Access Denied")
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


def search (request):
    if request.method == 'POST':
        search = request.POST.get('search-val', '')
        today = datetime.datetime.now()
        tournaments = Tournament.objects.filter(Q(name__icontains=search) | Q(address__icontains=search)).filter(datetime__gte=today).order_by('datetime')

        context = {
            'tournaments': tournaments,
            'pages': [0],
            'current_page': 1,
        }
        return render(request, 'tenis/index.html', context)
    return redirect('tenis.views.index')



def registered (request):
    if (not request.user.is_authenticated()):
        raise Http404("Access Denied")

    tournament_ids = []
    for x in Registration.objects.filter(player=request.user).values('tournament'):
        tournament_ids.append(x['tournament'])

    today = datetime.datetime.now()
    tournaments = Tournament.objects.filter(id__in=tournament_ids).filter(datetime__gte=today).order_by('datetime')

    context = {
        'tournaments': tournaments,
    }
    return render(request, 'tenis/registered.html', context)


def history (request):
    if (not request.user.is_authenticated()):
        raise Http404("Access Denied")

    tournament_ids = []
    for x in Registration.objects.filter(player=request.user).values('tournament'):
        tournament_ids.append(x['tournament'])

    today = datetime.datetime.now()
    tournaments = Tournament.objects.filter(id__in=tournament_ids).filter(datetime__lt=today).order_by('datetime')

    context = {
        'tournaments': tournaments,
    }
    return render(request, 'tenis/history.html', context)


def score (request):
    if (not request.user.is_authenticated()):
        raise Http404("Access Denied")

    if request.method == 'POST':
        match_id = request.POST.get('match-id', '')
        scoreYou = request.POST.get('scoreYou', '')
        scoreOpp = request.POST.get('scoreOpp', '')
        match = Match.objects.get(id=match_id)

        if (match.player1 != request.user and match.player2 != request.user):
            raise Http404("Access Denied")

        if (match.p1_points == -1 and match.p2_points == -1):
            if (match.player1 == request.user and match.p1_voted == False):
                match.p1_points = scoreYou
                match.p2_points = scoreOpp
                match.p1_voted = True
            elif (match.player2 == request.user and match.p2_voted == False):
                match.p2_points = scoreYou
                match.p1_points = scoreOpp
                match.p2_voted = True
        else:
            if (match.player1 == request.user and match.p1_voted == False):
                if (match.p1_points == int(scoreYou) and match.p2_points == int(scoreOpp)):
                    match.confirmed = True
                else:
                    match.p1_points = -1
                    match.p2_points = -1
                    match.p1_voted = False
                    match.p2_voted = False
            elif (match.player2 == request.user and match.p2_voted == False):
                if (match.p2_points == int(scoreYou) and match.p1_points == int(scoreOpp)):
                    match.confirmed = True
                else:
                    match.p1_points = -1
                    match.p2_points = -1
                    match.p1_voted = False
                    match.p2_voted = False
        match.save()
    return redirect('tenis.views.index')



def matches (request):
    if (not request.user.is_authenticated()):
        raise Http404("Access Denied")
    matches = Match.objects.all().filter((Q(player1=request.user) & Q(p1_voted=False)) | (Q(player2=request.user) & Q(p2_voted=False))).filter(confirmed=False)
    opponents = [match.player1 if match.player1 != request.user else match.player2 for match in matches]

    matches_info = zip(matches, opponents)

    context = {
        'matches_info': matches_info,
    }
    return render(request, 'tenis/matches.html', context)


def refresh (request):
    tournaments = Tournament.objects.all()
    today = datetime.datetime.now()

    for tournament in tournaments:
        if (tournament.datetime.replace(tzinfo=None) < today
        and tournament.stage == 0):
            if (tournament.participants_registered != tournament.participants_max):
                tournament.delete()
            else:
                players = [registration.player
                           for registration
                           in Registration.objects.filter(tournament=tournament).order_by('ranking')]

                for idx in range(int(len(players) / 2)):
                    player1 = players[idx]
                    player2 = players[len(players) - 1 - idx]

                    match = Match(
                            tournament = tournament,
                            stage = 1,
                            player1 = player1,
                            player2 = player2,
                            p1_points = -1,
                            p2_points = -1,
                            p1_voted = False,
                            p2_voted = False,
                            confirmed = False
                    )
                    match.save()
                tournament.stage = 1
                tournament.max_stage = int(math.log(len(players), 2))
                tournament.save()

        elif (tournament.stage > 0 and tournament.stage < tournament.max_stage):
            matchesInStage = int(int(math.pow(2, tournament.max_stage)) / int(math.pow(2, tournament.stage)))
            matches = [match
                       for match
                       in Match.objects.filter(Q(tournament=tournament)
                                             & Q(stage=tournament.stage)
                                             & Q(confirmed=True))]
            if (len(matches) == matchesInStage):
                players = []
                for match in matches:
                    if (match.p1_points > match.p2_points):
                        players.append(match.player1)
                    else:
                        players.append(match.player2)
                for idx in range(int(len(players) / 2)):
                    player1 = players[idx]
                    player2 = players[len(players) - 1 - idx]

                    match = Match(
                            tournament = tournament,
                            stage = tournament.stage + 1,
                            player1 = player1,
                            player2 = player2,
                            p1_points = -1,
                            p2_points = -1,
                            p1_voted = False,
                            p2_voted = False,
                            confirmed = False
                    )
                    match.save()
                tournament.stage += 1
                tournament.save()

        elif (tournament.stage > 0 and tournament.stage == tournament.max_stage):
            matches = Match.objects.filter(Q(tournament=tournament)
                                       & Q(stage=tournament.stage)
                                       & Q(confirmed=True))
            for match in matches:
                if (match.p1_points > match.p2_points):
                    tournament.winner = match.player1
                else:
                    tournament.winner = match.player2
            tournament.stage += 1
            tournament.save()

    return HttpResponse()
