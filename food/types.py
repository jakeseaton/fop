from common import enum

class MenuType(enum.Enum):
	standard = enum.Item(1, "Standard", code="A")
	nut_free = enum.Item(3, "Nut Free", code="B")
