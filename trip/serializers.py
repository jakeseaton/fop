from trip.models import Trip
from student.models import Leader
from rest_framework import serializers

class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = '__all__'

