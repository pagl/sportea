# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='logo',
            field=models.ImageField(upload_to=b'sportea/static/sport'),
        ),
    ]
