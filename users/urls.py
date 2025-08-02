from django.urls import path

from .apps import UsersConfig
from .views import Login, Logout, Profile, UsersCreate, RedactProfile

app_name = UsersConfig.name

urlpatterns = [
    path("", UsersCreate.as_view(), name="create"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/<int:pk>/", Profile.as_view(), name="profile"),
    path("redact/<int:pk>/", RedactProfile.as_view(), name="redact"),
]
