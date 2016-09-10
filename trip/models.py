from __future__ import unicode_literals

from django.db import models
from student.models import Leader

nullable = {
    "blank": True,
    "null": True
}

# Create your models here.
class Trip(models.Model):
    trip_number = models.IntegerField(**nullable)
    leaders = models.ManyToManyField(Leader)
    trip_year = models.IntegerField(**nullable)

    def __str__(self):
        return self.trip_number
