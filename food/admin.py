from django.contrib import admin
from models import *
map(admin.site.register, [FoodItem, Meal, Menu])

# Register your models here.
