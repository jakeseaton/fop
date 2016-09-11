from person.models import Student, Parent, Leader, Fopper
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'

class FopperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fopper
        fields = '__all__'
