from django.shortcuts import render

from rest_framework import generics, filters
from day.models import Day, Shelter, Trail
from day.serializers import DaySerializer, ShelterSerializer, TrailSerializer

class DayList(generics.ListAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['trip__number', 'is_first_day', 'is_last_day', 'day_number']

class DayDetail(generics.RetrieveUpdateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class ShelterList(generics.ListAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['name']

class ShelterDetail(generics.RetrieveUpdateAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class TrailList(generics.ListAPIView):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['name']

class TrailDetail(generics.RetrieveUpdateAPIView):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer

# Create your views here.
