# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 18:21
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0017_auto_20170215_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='events',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('batman', 'Batman'), ('ironman', 'Ironman'), ('flash', 'Flash'), ('arrow', 'Arrow'), ('blackwidow', 'Black Widow')], default=None, max_length=37),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Enter Valid Phone Number (10-digits)', regex='^\\d{10,10}$')]),
        ),
        migrations.AlterField(
            model_name='register',
            name='registd_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 15, 23, 51, 25, 187722)),
        ),
    ]
