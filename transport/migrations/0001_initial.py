# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trip', '0010_auto_20160911_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('trailhead', models.CharField(max_length=255)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus_stop', to='trip.Trip')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('number', models.IntegerField()),
                ('number_currently_assigned', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('year', models.IntegerField()),
                ('vechicle_type', models.IntegerField(choices=[(1, 'Bus'), (2, 'Van')], default=1)),
                ('loading_point', models.IntegerField(choices=[(1, 'Oxford Street'), (2, 'Memorial Loop')])),
                ('loading_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('bus_company_directions_link', models.CharField(blank=True, max_length=255, null=True)),
                ('trips', models.ManyToManyField(through='transport.Stop', to='trip.Trip')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='stop',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='transport.Vehicle'),
        ),
    ]
