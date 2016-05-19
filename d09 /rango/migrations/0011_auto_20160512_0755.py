# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0010_students_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='id',
        ),
        migrations.AlterField(
            model_name='students',
            name='card_no',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
