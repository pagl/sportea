from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Sport

def index (request):
    sports = Sport.objects.all()
    context = {'sports': sports}
    return render(request, 'app/index.html', context)


def log_in (request):
    return HttpResponse("LOGUJE BrACIE")
