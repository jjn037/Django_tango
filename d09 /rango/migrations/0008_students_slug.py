# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_students_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
