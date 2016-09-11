# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenis', '0008_auto_20160909_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='p1_vote',
            new_name='p1_points',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='p2_vote',
            new_name='p2_points',
        ),
        migrations.AddField(
            model_name='match',
            name='confirmed',
            field=models.BooleanField(default=b'False'),
        ),
    ]
