from django.db import models
from mixins import TimeStamp
from common import enum

class SolicitationMethod(enum.Enum):
    email = enum.Item(1, "Email")


class SolicitationCategory(enum.Enum):
    '''
    I have no clue what the categories of solicitation are.
    '''
    money = enum.Item(1, "Money")


# Create your models here.
class Solicitation(TimeStamp):
    person = models.ForeignKey("person.Person", related_name="solicitations")
    method = models.IntegerField(choices=SolicitationMethod, default=SolicitationMethod.email)
    category = models.IntegerField(choices=SolicitationCategory, default=SolicitationCategory.money)


class Donation(models.Model):
    person = models.ForeignKey("person.Person", related_name="donations")
    amount = models.IntegerField()
