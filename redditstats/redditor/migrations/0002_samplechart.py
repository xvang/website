# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redditor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleChart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.IntegerField()),
                ('boston_temp', models.DecimalField(max_digits=5, decimal_places=1)),
                ('houston_temp', models.DecimalField(max_digits=5, decimal_places=1)),
            ],
        ),
    ]
