# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 22:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0002_register_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='registd_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 2, 24, 22, 9, 17, 200938, tzinfo=utc)),
        ),
    ]
