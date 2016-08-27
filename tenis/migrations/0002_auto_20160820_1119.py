# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='sport',
        ),
        migrations.AlterField(
            model_name='match',
            name='player1',
            field=models.ForeignKey(related_name='player1', to='app.User', to_field=b'email'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player2',
            field=models.ForeignKey(related_name='player2', to='app.User', to_field=b'email'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.ForeignKey(to='app.User', to_field=b'email'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='organizer',
            field=models.ForeignKey(to='app.User', to_field=b'email'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
