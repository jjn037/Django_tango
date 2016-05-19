# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_remove_students_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='grade',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
