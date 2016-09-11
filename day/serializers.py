from day.models import Day, Shelter, Trail
from rest_framework import serializers

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'

class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fiels = '__all__'
