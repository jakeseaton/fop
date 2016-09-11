# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20160911_1302'),
        ('trip', '0008_remove_trip_leaders'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='leaders',
            field=models.ManyToManyField(related_name='trips', to='person.Leader'),
        ),
    ]
