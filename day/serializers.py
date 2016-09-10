from day.models import Day, Shelter, Trail
from rest_framework import serializers

class DaySerializer(serializers.HyperlinkedModelSerializer):
    trip = serializers.HyperlinkedRelatedField(
        many=False,
        view_name='day',
        queryset=Day.objects.all()
    )
    trails = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='trail',
        queryset=Trail.objects.all()
    )
    shelter_at_night = serializers.HyperlinkedRelatedField(
        many=False,
        view_name='shelter',
        queryset=Shelter.objects.all()
    )

    class Meta:
        model = Day
        fields = '__all__'

class ShelterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'

class TrailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trail
        fiels = '__all__'
