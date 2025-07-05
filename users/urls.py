from django.urls import path
from .apps import UsersConfig
from .views import UsersCreate

app_name = UsersConfig.name

urlpatterns = [
    path("", UsersCreate.as_view(), name="create"),
]
