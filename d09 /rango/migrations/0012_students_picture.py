# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0011_auto_20160512_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='picture',
            field=models.ImageField(default=b'media', upload_to=b'profile_images'),
        ),
    ]
