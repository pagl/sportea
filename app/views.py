from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response

from .models import Sport

def index (request):
    sports = Sport.objects.all()
    context = {'sports': sports}
    return render_to_response('app/index.html', context=context)


def log_in (request):
    return HttpResponse("LOGUJE BrACIE")
