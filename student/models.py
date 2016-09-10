from __future__ import unicode_literals

from common import enum
from django.db import models

# Create your models here.

nullable = {
    "blank": True,
    "null": True
}

class House(enum.Enum):
    quincy = enum.Item(1, "Quincy")

class Dorm(enum.Enum):
    mower = enum.Item(1, "Mower")

class SchoolType(enum.Enum):
    public = enum.Item(1, "Public")
    private = enum.Item(2, "Private")


# a live updating count of how many shirts you need to order
class TShirtSize(enum.Enum):
    extra_small = enum.Item(1, "Extra Small")
    small = enum.Item(2, "Small")
    medium = enum.Item(3, "Medium")
    large = enum.Item(4, "Large")
    extra_large = enum.Item(5, "Extra Large")


class State(enum.Enum):
    alabama = enum.Item(2, 'Alabama',
                abbrev='al',
                region_name='Alabama',
                timezone="CST")

    alaska = enum.Item(3, 'Alaska',
                abbrev='ak',
                region_name='Alaska',
                timezone="AKST")

    arizona = enum.Item(4, 'Arizona',
                abbrev='az',
                region_name='Arizona',
                timezone="MST")

    arkansas = enum.Item(5, 'Arkansas',
                abbrev='ar',
                region_name='Arkansas',
                timezone="CST")

    california = enum.Item(6, 'California',
                abbrev='ca',
                region_name='California',
                timezone="PST")

    colorado = enum.Item(7, 'Colorado',
                abbrev='co',
                region_name='Colorado',
                timezone="MST")

    connecticut = enum.Item(8, 'Connecticut',
                abbrev='ct',
                region_name='Connecticut',
                timezone="EST")

    delaware = enum.Item(9, 'Delaware',
                abbrev='de',
                region_name='Delaware',
                timezone="EST")

    district_of_columbia = enum.Item(10, 'Council of the District of Columbia',
                abbrev='dc',
                region_name='District of Columbia',
                timezone="EST")

    florida = enum.Item(11, 'Florida Legislature',
                abbrev='fl',
                region_name='Florida',
                timezone="EST")

    georgia = enum.Item(12, 'Georgia General Assembly',
                abbrev='ga',
                region_name='Georgia',
                timezone="EST")

    hawaii = enum.Item(13, 'Hawaii State Legislature',
                abbrev='hi',
                region_name='Hawaii',
                timezone="HST")

    idaho = enum.Item(14, 'Idaho State Legislature',
                abbrev='id',
                region_name='Idaho',
                timezone="MST")

    illinois = enum.Item(15, 'Illinois General Assembly',
                abbrev='il',
                region_name='Illinois',
                timezone="CST")

    indiana = enum.Item(16, 'Indiana General Assembly',
                abbrev='in',
                region_name='Indiana',
                timezone="EST")

    iowa = enum.Item(17, 'Iowa General Assembly',
                abbrev='ia',
                region_name='Iowa',
                timezone="CST")

    kansas = enum.Item(18, 'Kansas State Legislature',
                abbrev='ks',
                region_name='Kansas',
                timezone="CST")

    kentucky = enum.Item(19, 'Kentucky General Assembly',
                abbrev='ky',
                region_name='Kentucky',
                timezone="EST")

    louisiana = enum.Item(20, 'Louisiana Legislature',
                abbrev='la',
                region_name='Louisiana',
                timezone="CST")

    maine = enum.Item(21, 'Maine Legislature',
                abbrev='me',
                region_name='Maine',
                timezone="EST")

    maryland = enum.Item(22, 'Maryland General Assembly',
                abbrev='md',
                region_name='Maryland',
                timezone="EST")

    massachusetts = enum.Item(23, 'Massachusetts General Court',
                abbrev='ma',
                region_name='Massachusetts',
                timezone="EST")

    michigan = enum.Item(24, 'Michigan Legislature',
                abbrev='mi',
                region_name='Michigan',
                timezone="EST")

    minnesota = enum.Item(25, 'Minnesota State Legislature',
                abbrev='mn',
                region_name='Minnesota',
                timezone="CST")

    mississippi = enum.Item(26, 'Mississippi Legislature',
                abbrev='ms',
                region_name='Mississippi',
                timezone="CST")

    missouri = enum.Item(27, 'Missouri General Assembly',
                abbrev='mo',
                region_name='Missouri',
                timezone="CST")

    montana = enum.Item(28, 'Montana Legislature',
                abbrev='mt',
                region_name='Montana',
                timezone="MST")

    nebraska = enum.Item(29, 'Nebraska Legislature',
                abbrev='ne',
                region_name='Nebraska',
                timezone="CST")

    nevada = enum.Item(30, 'Nevada Legislature',
                abbrev='nv',
                region_name='Nevada',
                timezone="PST")

    new_hampshire = enum.Item(31, 'New Hampshire General Court',
                abbrev='nh',
                region_name='New Hampshire',
                timezone="EST")

    new_jersey = enum.Item(32, 'New Jersey Legislature',
                abbrev='nj',
                region_name='New Jersey',
                timezone="EST")

    new_mexico = enum.Item(33, 'New Mexico Legislature',
                abbrev='nm',
                region_name='New Mexico',
                timezone="MST")

    new_york = enum.Item(34, 'New York Legislature',
                abbrev='ny',
                region_name='New York',
                timezone="EST")

    north_carolina = enum.Item(35, 'North Carolina General Assembly',
                abbrev='nc',
                region_name='North Carolina',
                timezone="EST")

    north_dakota = enum.Item(36, 'North Dakota Legislative Assembly',
                abbrev='nd',
                region_name='North Dakota',
                timezone="CST")

    ohio = enum.Item(37, 'Ohio General Assembly',
                abbrev='oh',
                region_name='Ohio',
                timezone="EST")

    oklahoma = enum.Item(38, 'Oklahoma Legislature',
                abbrev='ok',
                region_name='Oklahoma',
                timezone="CST")

    oregon = enum.Item(39, 'Oregon Legislative Assembly',
                abbrev='or',
                region_name='Oregon',
                timezone="PST")

    pennsylvania = enum.Item(40, 'Pennsylvania General Assembly',
                abbrev='pa',
                region_name='Pennsylvania',
                timezone="EST")

    puerto_rico = enum.Item(41, 'Legislative Assembly of Puerto Rico',
                abbrev='pr',
                region_name='Puerto Rico',
                timezone="ATC")

    rhode_island = enum.Item(42, 'Rhode Island General Assembly',
                abbrev='ri',
                region_name='Rhode Island',
                timezone="EST")

    south_carolina = enum.Item(43, 'South Carolina Legislature',
                abbrev='sc',
                region_name='South Carolina',
                timezone="EST")

    south_dakota = enum.Item(44, 'South Dakota State Legislature',
                abbrev='sd',
                region_name='South Dakota',
                timezone="CST")

    tennessee = enum.Item(45, 'Tennessee General Assembly',
                abbrev='tn',
                region_name='Tennessee',
                timezone="CST")

    texas = enum.Item(46, 'Texas Legislature',
                abbrev='tx',
                region_name='Texas',
                timezone="CST")

    utah = enum.Item(47, 'Utah State Legislature',
                abbrev='ut',
                region_name='Utah',
                timezone="MST")

    vermont = enum.Item(48, 'Vermont General Assembly',
                abbrev='vt',
                region_name='Vermont',
                timezone="EST")

    virginia = enum.Item(49, 'Virginia General Assembly',
                abbrev='va',
                region_name='Virginia',
                timezone="EST")

    washington = enum.Item(50, 'Washington State Legislature',
                abbrev='wa',
                region_name='Washington',
                timezone="PST")

    west_virginia = enum.Item(51, 'West Virginia Legislature',
                abbrev='wv',
                region_name='West Virginia',
                timezone="EST")

    wisconsin = enum.Item(52, 'Wisconsin',
                abbrev='wi',
                region_name='Wisconsin',
                timezone="CST")

    wyoming = enum.Item(53, 'Wyoming',
                abbrev='wy',
                region_name='Wyoming',
                timezone="MST")

    @classmethod
    def from_state(cls, state):
        return cls.by_abbrev(state.abbrev.lower())

    @classmethod
    def publish_regions(cls):
        regions = [value for value in cls.publish().values() if value['key'] != 'federal']
        return sorted(regions, lambda x, y: x['value'] - y['value'])

    @staticmethod
    def return_all_abbrev():
        return [Region.by_value(reg).abbrev for reg in range(1, 54)]

    @staticmethod
    def return_all_vals():
        return range(1, 54)

    @staticmethod
    def all_state_vals():
        return range(2, 54)


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

    huid = models.IntegerField()

    tshirt_size = models.IntegerField(choices=TShirtSize, default=TShirtSize.large)
    # information from fun form
    #
    # room number?

    class Meta:
        abstract = True


class Fopper(Student):
    # trip = models.ForeignKey('')
    harvard_financial_aid = models.BooleanField(default=False)
    requests_fop_financial_aid = models.BooleanField(default=False)
    receives_fop_financial_aid = models.BooleanField(default=False)
    accepts_release_of_information = models.BooleanField(default=False)


class Leader(Student):
    is_sc = models.BooleanField(default=False)
    # if/when they were a fopper
    fopper = models.ForeignKey(Fopper, blank=True, null=True, related_name="was_fopper")
    pass
