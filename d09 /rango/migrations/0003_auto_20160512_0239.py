# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20160512_0237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='card_id',
            new_name='card_no',
        ),
    ]
