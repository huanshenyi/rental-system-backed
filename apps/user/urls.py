__author__ = "ハリネズミ"
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path('user', views.UserView.as_view(), name="user"),
    path("avatar", views.AvatarUploadView.as_view(), name="avatar")
]

