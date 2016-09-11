from django.db import models

from django.contrib.auth.models import User

class Tournament (models.Model):
    name = models.CharField(max_length=30)
    organizer = models.ForeignKey(User, related_name='organizer')
    datetime = models.DateTimeField()
    deadline = models.DateTimeField()
    address = models.CharField(max_length=50, default='Perth, Australia')
    participants_max = models.IntegerField()
    participants_registered = models.IntegerField()
    logo = models.ImageField(upload_to="tournament")
    stage = models.IntegerField(default=0)
    max_stage = models.IntegerField(default=0)
    winner = models.ForeignKey(User, null=True, blank=True, related_name='winner')


    def __str__ (self):
        return self.name


class Registration (models.Model):
    player = models.ForeignKey(User)
    tournament = models.ForeignKey(Tournament)
    license = models.CharField(max_length=50)
    ranking = models.CharField(max_length=50)

    def __str__ (self):
        return str(self.player) + ":" + str(self.tournament)


class Match (models.Model):
    tournament = models.ForeignKey(Tournament)
    stage = models.IntegerField()
    player1 = models.ForeignKey(User, related_name='player1')
    player2 = models.ForeignKey(User, related_name='player2')
    p1_points = models.IntegerField(default=-1)
    p2_points = models.IntegerField(default=-1)
    p1_voted = models.BooleanField(default='False')
    p2_voted = models.BooleanField(default='False')
    confirmed = models.BooleanField(default='False')

    def __str__ (self):
        return str(self.tournament) + "_" + str(self.player1) + ":" + str(self.player2)
