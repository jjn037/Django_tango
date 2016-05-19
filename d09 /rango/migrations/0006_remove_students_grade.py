# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_students_card_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='grade',
        ),
    ]
