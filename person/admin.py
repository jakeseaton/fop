from django.contrib import admin
from models import *

map(admin.site.register, [
	# Person,
	Parent,
	Student,
	Fopper,
	Leader
])
# Register your models here.
