# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenis', '0004_auto_20160903_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='email',
            new_name='player',
        ),
    ]
