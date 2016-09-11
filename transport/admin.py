from django.contrib import admin

from models import *
map(admin.site.register, [Stop, Vehicle])
# Register your models here.
