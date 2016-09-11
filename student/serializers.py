from rest_framework import serializers
from student.models import Fopper, Parent, Leader

class FopperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fopper
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'
