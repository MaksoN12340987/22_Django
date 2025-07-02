from django.urls import path

from .apps import UsersConfig

from .views import UsersList

app_name = UsersConfig.name

urlpatterns = [
    path("", UsersList.as_view(), name="home"),
]
