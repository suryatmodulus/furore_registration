# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 15:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0003_auto_20170215_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='incharge',
        ),
        migrations.AlterField(
            model_name='register',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 15, 21, 26, 45, 372664)),
        ),
    ]