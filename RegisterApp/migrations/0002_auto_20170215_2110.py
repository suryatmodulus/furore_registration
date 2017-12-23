# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 15:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='events',
            field=models.CharField(choices=[('batman', 'Batman'), ('ironman', 'Ironman'), ('flash', 'Flash'), ('arrow', 'Arrow'), ('avengers', 'Avengers')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='register',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 15, 21, 10, 58, 753520)),
        ),
    ]