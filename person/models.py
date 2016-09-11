
from django.db import models
from mixins import TimeStamp, nullable
from person.types import *
from trip.types import Difficulty, TripType

class Contact(models.Model):
    '''
    Abstract model for creating people that you can contact
    '''

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


class Donor(models.Model):
    '''
    A potential Donor
    '''
    do_not_solicit = models.BooleanField(default=False)
    email_only = models.BooleanField(default=False)
    special_donor = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Person(Contact, TimeStamp, Donor):
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    pass


class Parent(Person):
    '''
    A parent is an emergency contact or someone that you
    might solicit for a donation. They can have one or many students.

    (Should we also make them able to have been foppers themselves?)
    '''
    students = models.ManyToManyField("person.Student", related_name="parents")


class Student(Person):
    '''
    A student is a level above a Fopper, a Leader, or a Trainee
    '''

    harvard_email = models.CharField(max_length=255, **nullable)
    huid = models.IntegerField(**nullable)

    middle_name = models.CharField(max_length=255, **nullable)
    nickname = models.CharField(max_length=255, **nullable)

    # enums
    house = models.IntegerField(choices=House, **nullable)
    current_student_type = models.IntegerField(choices=StudentType)
    dorm = models.IntegerField(choices=Dorm, **nullable)

    # name of their high school
    school = models.CharField(max_length=255, **nullable)

    # public/private
    school_type = models.IntegerField(choices=SchoolType, default=SchoolType.public)

    height_feet = models.CharField(max_length=255, **nullable)
    height_inches = models.CharField(max_length=255, **nullable)
    tshirt_size = models.IntegerField(choices=TShirtSize, default=TShirtSize.large)

    # fuck the gender binary
    gender = models.IntegerField(choices=Gender)

    # we need to be able to compute their age
    birthdate = models.DateField(**nullable)
    graduation_year = models.IntegerField(**nullable)

    # would also love to add geopoints so that you can visualize the homes of a fop trip on a map

    significant_allergy = models.BooleanField(default=False)
    allergy_info = models.TextField(**nullable)
    food_restrictions = models.TextField(**nullable)

    pizza_slices = models.IntegerField(default=3)

class FinancialAid(models.Model):
    harvard_financial_aid = models.BooleanField(default=False)
    requests_fop_financial_aid = models.BooleanField(default=False)
    receives_fop_financial_aid = models.BooleanField(default=False)
    financial_aid_waiver = models.BooleanField(default=False)
    relative_need = models.IntegerField(**nullable)
    initial_fop_offer = models.IntegerField(**nullable)
    final_fop_award = models.IntegerField(**nullable)

    class Meta:
        abstract = True


class Fopper(Student, FinancialAid):
    # whether or not they got in to fop
    accepted = models.BooleanField(default=True)

    trip = models.ForeignKey('trip.Trip', related_name="participants", **nullable)

    swimming_ability = models.IntegerField(choices=SwimmingAbility, blank=True, null=True)

    preferred_backpacking_difficulty = models.IntegerField(choices=Difficulty, **nullable)
    preferred_switch_difficulty = models.IntegerField(choices=Difficulty, **nullable)
    preferred_service_difficulty = models.IntegerField(choices=Difficulty, **nullable)

    first_choice = models.IntegerField(choices=TripType, **nullable)
    second_choice = models.IntegerField(choices=TripType, **nullable)
    third_choice = models.IntegerField(choices=TripType, **nullable)
    fourth_choice = models.IntegerField(choices=TripType, **nullable)
    fifth_choice = models.IntegerField(choices=TripType, **nullable)

    switch_alt = models.BooleanField(default=False)
    service_alt = models.BooleanField(default=False)

    notes = models.TextField(**nullable)


    allergy = models.IntegerField(default=0, help_text="This is just for development of the algorithm")


class Leader(Student):
    is_sc = models.BooleanField(default=False)
    year_trained = models.IntegerField(**nullable)
    years_on_summer_staff = models.CharField(max_length=255, **nullable)
    years_on_steering_committee = models.CharField(max_length=255, **nullable)
    cc_number = models.CharField(max_length=255, **nullable)
    # if/when they were a fopper
    was_fopper = models.ForeignKey(Fopper, related_name="leader", **nullable)

    trained_switch = models.BooleanField(default=False)
    trained_service = models.BooleanField(default=False)

    preferred_difficulty = models.IntegerField(choices=Difficulty, **nullable)
    preferred_trip_type = models.IntegerField(choices=TripType, **nullable)

    active = models.BooleanField(default=True)
    # need to do certifications

    # Yay pictures!
    image = models.ImageField(**nullable)


# class Trainee(Student):
#     pass
