from django.shortcuts import render

from rest_framework import viewsets
from day.models import Day, Shelter, Trail
from day.serializers import DaySerializer, ShelterSerializer, TrailSerializer

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer

# Create your views here.
