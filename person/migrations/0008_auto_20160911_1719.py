# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0007_auto_20160911_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fopper',
            name='trip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='trip.Trip'),
        ),
    ]
