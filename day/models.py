from __future__ import unicode_literals

from django.db import models

from common import enum

from student.models import State
from trip.models import Trip
# Create your models here.

class Difficulty(enum.Enum):
    A = enum.Item(1, "A Trip")
    B = enum.Item(2, "B Trip")
    C = enum.Item(3, "C Trip")

nullable = {
    "blank": True,
    "null": True
}

# this should be admin maintained
class Shelter(models.Model):
    name = models.CharField(max_length=255, **nullable)
    state = State

    def __str__(self):
        return self.name

# this should be admin mainained
class Trail(models.Model):
    name = models.CharField(max_length=255, **nullable)
    state = State

    def __str__(self):
        return self.name

class Day(models.Model):
    trip = models.ForeignKey(Trip, related_name="days")
    is_first_day = models.BooleanField(default=False)
    is_last_day = models.BooleanField(default=False)
    day_number = models.IntegerField(**nullable)
    dropoff_info = models.CharField(max_length=255, **nullable)
    distance = models.IntegerField(**nullable)
    elev_up = models.IntegerField(**nullable)
    elev_down = models.IntegerField(**nullable)
    shelter_at_night = models.ForeignKey(Shelter, related_name="trip_days", **nullable)
    trails = models.ManyToManyField(Trail, related_name="trip_days", **nullable)
    water_on_trail = models.CharField(max_length=255, **nullable)
    views_and_notes = models.CharField(max_length=255, **nullable)
    campsite_and_water = models.CharField(max_length=255, **nullable)
    pickup_info = models.CharField(max_length=255, **nullable)
    difficulty = Difficulty
    cambridge_to_trail_distance = models.IntegerField(**nullable)

    def __str__(self):
        return "FOP " + self.trip.trip_number + ": Day " + self.day_number
