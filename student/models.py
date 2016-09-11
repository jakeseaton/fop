from __future__ import unicode_literals

from django.db import models
from trip.types import Difficulty, TripType
from student.types import *
# Create your models here.

nullable = {
    "blank": True,
    "null": True
}


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, **nullable)
    phone = models.CharField(max_length=255, **nullable)

    # geograpgic data so that we can
    country = models.CharField(max_length=255, default="USA", **nullable)
    address = models.CharField(max_length=255, **nullable)
    zipcode = models.IntegerField(**nullable)
    state = models.CharField(max_length=255, **nullable)
    city = models.CharField(max_length=255, **nullable)

    class Meta:
        abstract = True


class Parent(Contact):
    child = models.ForeignKey("student.Fopper", related_name="parent")


class Student(Contact):

    middle_name = models.CharField(max_length=255, **nullable)
    nickname = models.CharField(max_length=255, **nullable)

    # enums
    house = models.IntegerField(choices=House, **nullable)
    dorm = models.IntegerField(choices=Dorm, **nullable)

    school = models.CharField(max_length=255, **nullable)
    school_type = models.IntegerField(choices=SchoolType, default=SchoolType.public)

    height_feet = models.CharField(max_length=255, **nullable)
    height_inches = models.CharField(max_length=255, **nullable)

    # this is going to be important for matching people...would be great if it could
    # be an enum but fuck the gender binary
    gender = models.CharField(max_length=255, **nullable)

    birthdate = models.DateField(**nullable)
    graduation_year = models.IntegerField(**nullable)
    # would also love to add geopoints so that you can visualize the homes of a fop trip on a map

    huid = models.IntegerField(**nullable)

    tshirt_size = models.IntegerField(choices=TShirtSize, default=TShirtSize.large)

    

    # information from fun form
    #
    # room number?

    class Meta:
        abstract = True


class Fopper(Student):
    trip = models.ForeignKey('trip.Trip', null=True)
    harvard_financial_aid = models.BooleanField(default=False)
    requests_fop_financial_aid = models.BooleanField(default=False)
    receives_fop_financial_aid = models.BooleanField(default=False)
    accepts_release_of_information = models.BooleanField(default=False)
    swimming_ability = models.IntegerField(choices=SwimmingAbility, blank=True, null=True)

    preferred_backpacking_difficulty = models.IntegerField(choices=Difficulty, **nullable)
    preferred_switch_difficulty = models.IntegerField(choices=Difficulty, **nullable)
    preferred_service_difficulty = models.IntegerField(choices=Difficulty, **nullable)

    first_choice = models.IntegerField(choices=TripType, **nullable)
    second_choice = models.IntegerField(choices=TripType, **nullable)
    third_choice = models.IntegerField(choices=TripType, **nullable)
    fourth_choice = models.IntegerField(choices=TripType, **nullable)
    fifth_choice = models.IntegerField(choices=TripType, **nullable)


class Leader(Student):
    is_sc = models.BooleanField(default=False)
    # if/when they were a fopper
    fopper = models.ForeignKey(Fopper, blank=True, null=True, related_name="was_fopper")
    switch = models.BooleanField(default=False)
    preferred_difficulty = models.IntegerField(choices=Difficulty, **nullable)
    preferred_trip_type = models.IntegerField(choices=TripType, **nullable)

    image = models.ImageField(**nullable)
