from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers
from trip.views import TripList
from day.views import DayList, ShelterList, TrailList
from student.views import FopperList, ParentList, LeaderList


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^planner/', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^trip/$', TripList.as_view()),
    url(r'^day/$', DayList.as_view()),
    url(r'^shelter/$', ShelterList.as_view()),
    url(r'^trail/$', TrailList.as_view()),
    url(r'^shelter/$', ShelterList.as_view()),
    url(r'^fopper/$', FopperList.as_view()),
    url(r'^parent/$', ParentList.as_view()),
    url(r'^leader/$', LeaderList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^student/', include('student.urls')),
]
