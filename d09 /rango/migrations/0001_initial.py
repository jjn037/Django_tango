# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
                ('id_card', models.IntegerField()),
                ('sex', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
    ]
