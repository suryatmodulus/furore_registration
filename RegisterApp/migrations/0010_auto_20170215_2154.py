# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 16:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0009_auto_20170215_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='register',
            name='registered_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 15, 21, 54, 7, 494490)),
        ),
    ]