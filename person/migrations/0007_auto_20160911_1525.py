# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_auto_20160911_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fopper',
            old_name='accepts_release_of_information',
            new_name='financial_aid_waiver',
        ),
        migrations.AddField(
            model_name='fopper',
            name='final_fop_award',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fopper',
            name='initial_fop_offer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fopper',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fopper',
            name='relative_need',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='pizza_slices',
            field=models.IntegerField(default=3),
        ),
    ]
