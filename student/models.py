from __future__ import unicode_literals

from common import enum
from django.db import models

# Create your models here.


class House(enum.Enum):
    quincy = enum.Item(1, "Quincy")


class Dorm(enum.Enum):
    mower = enum.Item(1, "Mower")


class Student(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    house = models.IntegerField(choices=House, blank=True, null=True)
    dorm = models.IntegerField(choices=Dorm, blank=True, null=True)

    # hometown
    #
    # information from fun form
    #
    # room number?

    class Meta:
        abstract = True


class Fopper(models.Model):
    pass


class Leader(Student):
    is_sc = models.BooleanField(default=False)
    pass
