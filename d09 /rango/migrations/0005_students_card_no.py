# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_remove_students_card_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='card_no',
            field=models.IntegerField(default=0),
        ),
    ]
