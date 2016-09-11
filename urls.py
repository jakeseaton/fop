from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers
from trip.views import TripViewSet
from day.views import DayViewSet, ShelterViewSet, TrailViewSet
from student.views import FopperViewSet, ParentViewSet, LeaderViewSet

router = routers.DefaultRouter()
router.register(r'trip', TripViewSet)
router.register(r'day', DayViewSet)
router.register(r'shelter', ShelterViewSet)
router.register(r'trail', TrailViewSet)
router.register(r'fopper', FopperViewSet)
router.register(r'parent', ParentViewSet)
router.register(r'leader', LeaderViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^student/', include('student.urls')),
]
