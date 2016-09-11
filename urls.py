from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers
from trip.views import TripList, TripDetail
from day.views import DayList, DayDetail, ShelterList, ShelterDetail, TrailList, TrailDetail
from person.views import StudentList, StudentDetail, LeaderList, LeaderDetail, ParentList, ParentDetail, FopperList, FopperDetail

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^planner/', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^trip/$', TripList.as_view()),
    url(r'^trip/(?P<pk>[0-9]+)$', TripDetail.as_view()),
    url(r'^day/$', DayList.as_view()),
    url(r'^day/(?P<pk>[0-9]+)$', DayDetail.as_view()),
    url(r'^shelter/$', ShelterList.as_view()),
    url(r'^shelter/(?P<pk>[0-9]+)$', ShelterDetail.as_view()),
    url(r'^trail/$', TrailList.as_view()),
    url(r'^trail/(?P<pk>[0-9]+)$', TrailDetail.as_view()),
    url(r'^student/$', StudentList.as_view()),
    url(r'^student/(?P<pk>[0-9]+)$', StudentDetail.as_view()),
    url(r'^leader/$', LeaderList.as_view()),
    url(r'^leader/(?P<pk>[0-9]+)$', LeaderDetail.as_view()),
    url(r'^parent/$', ParentList.as_view()),
    url(r'^parent/(?P<pk>[0-9]+)$', ParentDetail.as_view()),
    url(r'^fopper/$', FopperList.as_view()),
    url(r'^fopper/(?P<pk>[0-9]+)$', FopperDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
