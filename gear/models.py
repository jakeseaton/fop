from __future__ import unicode_literals

from django.db import models
from mixins import TimeStamp

# Create your models here.

class Item(TimeStamp):
    name = models.CharField(max_length=255)
    count = models.IntegerField(default=0)


class Request(TimeStamp):
    status = models.BooleanField(default=False)
    person = models.ForeignKey("person.Student", related_name="gear_requests")
    gear = models.ForeignKey(Item, related_name="requests")
