from django.contrib import admin

from .models import User, Tournament, Match, Registration

admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(Registration)
