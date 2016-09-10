from trip.models import Trip
from student.models import Leader
from rest_framework import serializers

class TripSerializer(serializers.HyperlinkedModelSerializer):
    leaders = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='leader',
        queryset=Leader.objects.all()
    )

    class Meta:
        model = Trip
        fields = '__all__'

