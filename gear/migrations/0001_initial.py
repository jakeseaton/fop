# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0004_auto_20160911_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('gear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='gear.Gear')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
