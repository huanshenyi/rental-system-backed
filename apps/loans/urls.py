__author__ = "ハリネズミ"
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter(trailing_slash=False)
router.register("period", views.PeriodViewSet, basename="period")

app_name = "loans"

urlpatterns = [

] + router.urls

