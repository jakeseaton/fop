from __future__ import unicode_literals

from django.db import models
from student.models import Leader
from trip.types import Difficulty

nullable = {
    "blank": True,
    "null": True
}


# Create your models here.
class Trip(models.Model):
    number = models.IntegerField(**nullable)
    leaders = models.ManyToManyField(Leader, related_name="trips")
    year = models.IntegerField(**nullable)
    difficulty = models.IntegerField(choices=Difficulty, **nullable)
    description = models.CharField(max_length=255, **nullable)

    def __str__(self):
        return "Fop %s (%s)" % (self.number, self.year)
