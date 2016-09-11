from __future__ import unicode_literals

from django.db import models

from common import enum

from person.types import State
from trip.models import Trip
# Create your models here.


nullable = {
    "blank": True,
    "null": True
}


# this should be admin maintained
class Shelter(models.Model):
    name = models.CharField(max_length=255, **nullable)
    water = models.BooleanField(default=True)
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
    has_good_water = models.BooleanField(default=False)
    water_description = models.TextField(**nullable)

    def __str__(self):
        return self.name


class DayType(enum.Enum):
    drop_off = enum.Item(1, "Drop Off")
    hike = enum.Item(2, "Hike")
    switch = enum.Item(3, "Switch")
    canoe = enum.Item(4, "Canoe")
    service = enum.Item(5, "Service")
    pick_up = enum.Item(6, "Pick Up")


class Day(models.Model):
    # aka activity
    day_type = models.IntegerField(choices=DayType, default=DayType.hike)

    trip = models.ForeignKey(Trip, related_name="days")
    trails = models.ManyToManyField(Trail, related_name="trip_days")
    shelter_at_night = models.ForeignKey(Shelter, related_name="trip_days", **nullable)

    is_first_day = models.BooleanField(default=False)
    is_last_day = models.BooleanField(default=False)
    is_national_forest = models.BooleanField(default=False)

    day_number = models.IntegerField(**nullable)
    date = models.DateField(**nullable)
    dropoff_info = models.TextField(**nullable)
    distance = models.IntegerField(**nullable)
    elev_up = models.IntegerField(**nullable)
    elev_down = models.IntegerField(**nullable)
    water_on_trail = models.BooleanField(default=False)
    water_on_trail_description = models.TextField(**nullable)
    views_and_notes = models.TextField(**nullable)
    campsite_and_water = models.TextField(**nullable)
    pickup_info = models.TextField(**nullable)
    cambridge_to_trail_distance = models.IntegerField(**nullable)

    def __str__(self):
        return "FOP " + str(self.trip.number) + ": Day " + str(self.day_number)
