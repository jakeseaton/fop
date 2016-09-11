from django.shortcuts import render

from rest_framework import generics, filters
from day.models import Day, Shelter, Trail
from day.serializers import DaySerializer, ShelterSerializer, TrailSerializer

class DayList(generics.ListAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['trip__number', 'is_first_day', 'is_last_day', 'day_number']

class ShelterList(generics.ListAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['name']

class TrailList(generics.ListAPIView):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['name']

# Create your views here.
