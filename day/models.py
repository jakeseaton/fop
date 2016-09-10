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
    has_good_water = models.BooleanField(default=False)
    water_description = models.TextField(**nullable)
    has_platforms = models.BooleanField(default=False)
    sleeping_space_description = models.TextField(**nullable)
    has_privy = models.BooleanField(default=False)
    can_reserve = models.BooleanField(default=False)
    reservation_cost = models.IntegerField(**nullable)
    amc_maintained = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# this should be admin maintained
class Trail(models.Model):
    name = models.CharField(max_length=255, **nullable)
    state = State
    has_good_water = models.BooleanField(default=False)
    water_description = models.TextField(**nullable)

    def __str__(self):
        return self.name

class Day(models.Model):
    trip = models.ForeignKey(Trip, related_name="days")
    is_first_day = models.BooleanField(default=False)
    is_last_day = models.BooleanField(default=False)
    day_number = models.IntegerField(**nullable)
    dropoff_info = models.TextField(**nullable)
    distance = models.IntegerField(**nullable)
    elev_up = models.IntegerField(**nullable)
    elev_down = models.IntegerField(**nullable)
    shelter_at_night = models.ForeignKey(Shelter, related_name="trip_days", **nullable)
    trails = models.ManyToManyField(Trail, related_name="trip_days")
    water_on_trail = models.BooleanField(default=False)
    water_on_trail_description = models.TextField(**nullable)
    views_and_notes = models.TextField(**nullable)
    campsite_and_water = models.TextField(**nullable)
    pickup_info = models.TextField(**nullable)
    difficulty = Difficulty
    cambridge_to_trail_distance = models.IntegerField(**nullable)

    def __str__(self):
        return "FOP " + self.trip.trip_number + ": Day " + self.day_number
