# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenis', '0010_auto_20160911_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='p1_voted',
            field=models.BooleanField(default=b'False'),
        ),
        migrations.AddField(
            model_name='match',
            name='p2_voted',
            field=models.BooleanField(default=b'False'),
        ),
    ]
