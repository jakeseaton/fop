from __future__ import unicode_literals

from django.db import models
from person.models import Leader
from trip.types import Difficulty, TripType
from food.types import MenuType
from common import enum

nullable = {
    "blank": True,
    "null": True
}


class BaseCamp(enum.Enum):
    maine = enum.Item(1, "Maine")
    new_hampshire = enum.Item(2, "New Hampshire")

# Create your models here.
class Trip(models.Model):
    number = models.IntegerField(**nullable)
    description = models.CharField(max_length=255, **nullable)
    leaders = models.ManyToManyField(Leader, related_name="trips")
    year = models.IntegerField(**nullable)

    basecamp = models.IntegerField(choices=BaseCamp, **nullable)
    max_people = models.IntegerField(default=10)

    # current people can be calculated with leaders plus foppers
    difficulty = models.IntegerField(choices=Difficulty, **nullable)
    trip_type = models.IntegerField(choices=TripType, **nullable)
    luggage_room = models.CharField(max_length=255, **nullable)
    sleeping_room = models.CharField(max_length=255, **nullable)

    # drop_off_location
    # pick_up_location
    pick_up_time = models.TimeField(**nullable)
    plb = models.CharField(max_length=255, **nullable)
    menu = models.IntegerField(choices=MenuType, default=MenuType.standard)

    active = models.BooleanField(default=True)

    liason = models.CharField(max_length=255, **nullable)

    emergency_cell_phone = models.CharField(max_length=255, **nullable)
    #trainer_cell_phone

    def __str__(self):
        return "Fop %s (%s)" % (self.number, self.year)

    daily_cost = models.FloatField(**nullable)
    def compute_daily_cost(self):
        '''
        Coz wants to be able to compute the average daily cost of the trip
        '''
        return 0

    def compute_leader_user_days(self):
        return self.days.filter(is_nationa_forest=True).count() * self.leaders.count()

    def compute_participant_user_days(self):
        return self.days.filter(is_nationa_forest=True).count() * self.participants.count()

    def compute_total_user_days(self):
        return self.compute_participant_user_days() + self.computer_leader_user_days()

    def compute_trip_revenue(self):
        tuition = 400
        return self.participants.count() * tuition

