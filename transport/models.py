from __future__ import unicode_literals

from django.db import models

from common import enum
from mixins import *

class VehicleType(enum.Enum):
    bus = enum.Item(1, "Bus")
    van = enum.Item(2, "Van")

class LoadingPoint(enum.Enum):
    oxford_street = enum.Item(1, "Oxford Street")
    memorial_loop = enum.Item(2, "Memorial Loop")


class Stop(models.Model):
    number = models.IntegerField()
    trip = models.ForeignKey("trip.Trip", on_delete=models.CASCADE, related_name="bus_stop")
    vehicle = models.ForeignKey("transport.Vehicle", on_delete=models.CASCADE, related_name="stops")

    latitude = models.FloatField()
    longitude = models.FloatField()

    trailhead = models.CharField(max_length=255)


class Vehicle(TimeStamp):
    active = models.BooleanField(default=True)
    number = models.IntegerField()
    # we should be able to compute this programatically
    number_currently_assigned = models.IntegerField()
    capacity = models.IntegerField()
    year = models.IntegerField()

    trips = models.ManyToManyField("trip.Trip", through=Stop)

    vechicle_type = models.IntegerField(choices=VehicleType, default=VehicleType.bus)
    loading_point = models.IntegerField(choices=LoadingPoint)
    loading_time = models.TimeField()
    departure_time = models.TimeField()

    notes = models.TextField(**nullable)
    bus_company_directions_link = models.CharField(max_length=255, **nullable)

# Create your models here.
