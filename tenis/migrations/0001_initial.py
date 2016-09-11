# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stage', models.IntegerField()),
                ('p1_points', models.IntegerField(default=-1)),
                ('p2_points', models.IntegerField(default=-1)),
                ('p1_voted', models.BooleanField(default=b'False')),
                ('p2_voted', models.BooleanField(default=b'False')),
                ('confirmed', models.BooleanField(default=b'False')),
                ('player1', models.ForeignKey(related_name='player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(related_name='player2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license', models.CharField(max_length=50)),
                ('ranking', models.CharField(max_length=50)),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('datetime', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('address', models.CharField(default=b'Perth, Australia', max_length=50)),
                ('participants_max', models.IntegerField()),
                ('participants_registered', models.IntegerField()),
                ('logo', models.ImageField(upload_to=b'tournament')),
                ('stage', models.IntegerField(default=0)),
                ('max_stage', models.IntegerField(default=0)),
                ('organizer', models.ForeignKey(related_name='organizer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='tournament',
            field=models.ForeignKey(to='tenis.Tournament'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(to='tenis.Tournament'),
        ),
    ]
