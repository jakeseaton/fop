from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, filters

from student.serializers import FopperSerializer, ParentSerializer, LeaderSerializer
from student.models import Fopper, Parent, Leader

# Create your views here.

class FopperList(generics.ListAPIView):
    queryset = Fopper.objects.all()
    serializer_class = FopperSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['last_name', 'first_name']

class ParentList(generics.ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['last_name', 'first_name']

class LeaderList(generics.ListAPIView):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['last_name', 'first_name']


def index(request):
    return render(request, "form_base.html", {})
    return HttpResponse("Hello, world. You're at the polls index.")
