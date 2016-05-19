# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='id_card',
            new_name='card_id',
        ),
    ]
