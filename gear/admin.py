from django.contrib import admin
from models import *

map(admin.site.register, [Gear, Request])
# Register your models here.
