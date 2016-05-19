# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20160512_0239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='card_no',
        ),
    ]
