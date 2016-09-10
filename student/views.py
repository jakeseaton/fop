from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from student.serializers import FopperSerializer, ParentSerializer, LeaderSerializer
from student.models import Fopper, Parent, Leader

# Create your views here.

class FopperViewSet(viewsets.ModelViewSet):
    queryset = Fopper.objects.all()
    serializer_class = FopperSerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class LeaderViewSet(viewsets.ModelViewSet):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer


def index(request):
    return render(request, "form_base.html", {})
    return HttpResponse("Hello, world. You're at the polls index.")
