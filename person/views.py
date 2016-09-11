from django.shortcuts import render

from person.models import Student, Leader, Parent, Fopper
from person.serializers import StudentSerializer, LeaderSerializer, ParentSerializer, FopperSerializer

from rest_framework import filters, generics

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['first_name', 'last_name']

class StudentDetail(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class LeaderList(generics.ListAPIView):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['first_name', 'last_name']

class LeaderDetail(generics.RetrieveUpdateAPIView):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer

class ParentList(generics.ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['first_name', 'last_name']

class ParentDetail(generics.RetrieveUpdateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['first_name', 'last_name']

class FopperList(generics.ListAPIView):
    queryset = Fopper.objects.all()
    serializer_class = FopperSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['first_name', 'last_name']

class FopperDetail(generics.RetrieveUpdateAPIView):
    queryset = Fopper.objects.all()
    serializer_class = FopperSerializer

# Create your views here.
