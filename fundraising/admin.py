from django.contrib import admin

# Register your models here.
from models import Solicitation, Donation

admin.site.register(Solicitation)
admin.site.register(Donation)