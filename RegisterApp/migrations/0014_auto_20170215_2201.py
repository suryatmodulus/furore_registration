# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 16:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0013_auto_20170215_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='date',
        ),
        migrations.AddField(
            model_name='register',
            name='registd_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 15, 22, 1, 32, 267967)),
        ),
    ]