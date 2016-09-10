from rest_framework import serializers
from student.models import Fopper, Parent, Leader

class FopperSerializer(serializers.HyperlinkedModelSerializer):
    trip = serializers.HyperlinkedRelatedField(
        many=False,
        view_name='trip',
        queryset=Fopper.objects.all()
    )

    class Meta:
        model = Fopper
        fields = '__all__'

class ParentSerializer(serializers.HyperlinkedModelSerializer):
    child = serializers.HyperlinkedRelatedField(
        many=False,
        view_name='fopper',
        queryset=Fopper.objects.all()
    )

    class Meta:
        model = Parent
        fields = '__all__'

class LeaderSerializer(serializers.HyperlinkedModelSerializer):
    fopper = serializers.HyperlinkedRelatedField(
        many=False,
        view_name='fopper',
        queryset=Fopper.objects.all()
    )

    class Meta:
        model = Leader
        fields = '__all__'
