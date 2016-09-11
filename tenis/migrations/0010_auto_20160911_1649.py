# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenis', '0009_auto_20160911_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='p1_points',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='match',
            name='p2_points',
            field=models.IntegerField(default=-1),
        ),
    ]
