from django.shortcuts import render

from rest_framework import generics
from day.models import Day, Shelter, Trail
from day.serializers import DaySerializer, ShelterSerializer, TrailSerializer

class DayList(generics.ListAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class ShelterList(generics.ListAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class TrailList(generics.ListAPIView):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer

# Create your views here.
