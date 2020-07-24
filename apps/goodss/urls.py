__author__ = "ハリネズミ"
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
router = DefaultRouter(trailing_slash=False)
router.register("goods", views.GoodsViewSet, basename="goods")


app_name = "goodss"

urlpatterns = [

] + router.urls
