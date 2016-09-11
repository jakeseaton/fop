from __future__ import unicode_literals

from django.db import models
from mixins import TimeStamp, nullable

from common import enum


class MedFormStatus(enum.Enum):
    cleared = enum.Item(1, "Cleared")


class CertificationType(enum.Enum): 
    cpr = enum.Item(1, "CPR")
    wfa = enum.Item(2, "WFA")
    wfr = enum.Item(3, "WFR")
    emt = enum.Item(4, "EMT")
    driver = enum.Item(5, "Driver")


class Certification(TimeStamp):
    certification_type = models.IntegerField(choices=CertificationType, default=CertificationType.wfa)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    source = models.CharField(max_length=255, default="SOLO")


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

