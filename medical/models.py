from __future__ import unicode_literals

from django.db import models
from mixins import TimeStamp, nullable

from common import enum

class MedFormStatus(enum.Enum):
    cleared = enum.Item(1, "Cleared")


class MedForm(TimeStamp):
    person = models.ForeignKey("person.Person", related_name="med_forms")
    status = models.IntegerField(default=MedFormStatus.cleared)
    form_pdf = models.FileField(**nullable)
    date_of_physical = models.DateField()
    page_1_received = models.BooleanField(default=False)
    page_2_received = models.BooleanField(default=False)
    ins_card_received = models.BooleanField(default=False)
    page_1_incomplete = models.BooleanField(default=False)
    page_2_incomplete = models.BooleanField(default=False)

    notes = models.TextField(**nullable)
    
    # food_restrictions = models.TextField(**nullable)
    

    # # right now there are in student 
    # pertinent_conditions = models.TextField(**nullable)
    # significant_allergy = models.BooleanField(default=False)
    # allergy_info = models.TextField(**nullable)

