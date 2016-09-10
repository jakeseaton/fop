# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_fopper_leader_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='fopper',
            name='accepts_release_of_information',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fopper',
            name='harvard_financial_aid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fopper',
            name='receives_fop_financial_aid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fopper',
            name='requests_fop_financial_aid',
            field=models.BooleanField(default=False),
        ),
    ]