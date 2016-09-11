# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenis', '0007_tournament_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='license',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='ranking',
            field=models.CharField(max_length=50),
        ),
    ]
