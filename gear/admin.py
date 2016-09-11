from django.contrib import admin
from models import *

map(admin.site.register, [Item, Request])
# Register your models here.
