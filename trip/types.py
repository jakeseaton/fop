from common import enum


class Difficulty(enum.Enum):
    A = enum.Item(1, "A Trip")
    B = enum.Item(2, "B Trip")
    C = enum.Item(3, "C Trip")


class TripType(enum.Enum):
    backpacking = enum.Item(1, "Backpacking")
    switch = enum.Item(2, "Switch Canoe")
    service = enum.Item(3, "Switch Service")
    site = enum.Item(4, "Site-Based Service")
    cabin = enum.Item(5, "Cabin-Based")
