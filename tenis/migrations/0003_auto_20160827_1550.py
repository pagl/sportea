# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenis', '0002_auto_20160820_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='logo',
            field=models.ImageField(upload_to=b'tournament'),
        ),
    ]
