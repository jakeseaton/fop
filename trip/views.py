from django.shortcuts import render
from rest_framework import generics, filters
from trip.serializers import TripSerializer
from trip.models import Trip

# Create your views here.
class TripList(generics.ListAPIView):
    """
    API endpoint that allows accessing trip information
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['number', 'year']
