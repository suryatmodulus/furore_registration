# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 16:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0006_auto_20170215_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 15, 21, 31, 49, 959054)),
        ),
    ]
