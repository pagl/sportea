# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stage', models.IntegerField()),
                ('p1_vote', models.IntegerField()),
                ('p2_vote', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license', models.CharField(unique=True, max_length=50)),
                ('ranking', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('sport', models.CharField(max_length=30)),
                ('datetime', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('participants_max', models.IntegerField()),
                ('participants_registered', models.IntegerField()),
                ('logo', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('activation_code', models.CharField(max_length=100)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='organizer',
            field=models.ForeignKey(to='tenis.User', to_field=b'email'),
        ),
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.ForeignKey(to='tenis.User', to_field=b'email'),
        ),
        migrations.AddField(
            model_name='registration',
            name='tournament',
            field=models.ForeignKey(to='tenis.Tournament'),
        ),
        migrations.AddField(
            model_name='match',
            name='player1',
            field=models.ForeignKey(related_name='player1', to='tenis.User', to_field=b'email'),
        ),
        migrations.AddField(
            model_name='match',
            name='player2',
            field=models.ForeignKey(related_name='player2', to='tenis.User', to_field=b'email'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(to='tenis.Tournament'),
        ),
    ]
