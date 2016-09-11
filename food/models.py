from __future__ import unicode_literals

from django.db import models

# Create your models here.


class FoodItem(models.Model): 
    '''
    All of the food items that we have to take with us
    '''
    name = models.CharField(max_length=255)
    perishable = models.BooleanField(default=False)


class Meal(models.Model):
    '''
    The various meals that we make
    '''
    ingredients = models.ManyToManyField(FoodItem, related_name="meals")


class Menu(models.Model):
	meals = models.ManyToManyField(Meal)

# class Allergy(models.Model):
#     ingredient = models.ManyToManyField(Food)
#     # some sort of enum food of the different types of allergies
#     pass
