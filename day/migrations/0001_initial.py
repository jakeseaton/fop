# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trip', '0003_auto_20160910_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_first_day', models.BooleanField(default=False)),
                ('is_last_day', models.BooleanField(default=False)),
                ('day_number', models.IntegerField(blank=True, null=True)),
                ('dropoff_info', models.CharField(blank=True, max_length=255, null=True)),
                ('distance', models.IntegerField(blank=True, null=True)),
                ('elev_up', models.IntegerField(blank=True, null=True)),
                ('elev_down', models.IntegerField(blank=True, null=True)),
                ('water_on_trail', models.CharField(blank=True, max_length=255, null=True)),
                ('views_and_notes', models.CharField(blank=True, max_length=255, null=True)),
                ('campsite_and_water', models.CharField(blank=True, max_length=255, null=True)),
                ('pickup_info', models.CharField(blank=True, max_length=255, null=True)),
                ('cambridge_to_trail_distance', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='shelter_at_night',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trip_days', to='day.Shelter'),
        ),
        migrations.AddField(
            model_name='day',
            name='trails',
            field=models.ManyToManyField(related_name='trip_days', to='day.Trail'),
        ),
        migrations.AddField(
            model_name='day',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='trip.Trip'),
        ),
    ]
