# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenis', '0006_auto_20160907_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='address',
            field=models.CharField(default=b'Perth Australia', max_length=50),
        ),
    ]
