from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Food(models.Model): 
    '''
    All of the food items that we have to take with us
    '''
    pass


class Meal(models.Model):
    '''
    The various meals that we make
    '''
    ingredients = models.ManyToManyField(Food)


class Allergy(models.Model):
    ingredient = models.ManyToManyField(Food)
    # some sort of enum food of the different types of allergies
    pass
