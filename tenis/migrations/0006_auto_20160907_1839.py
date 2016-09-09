# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenis', '0005_auto_20160903_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='longitude',
        ),
    ]
