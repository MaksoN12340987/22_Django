from django.contrib import admin # type: ignore
from django.urls import path # type: ignore

from .views import PostsListView

from blog.apps import BlogProjectName
app_name = BlogProjectName.name

urlpatterns = [
    path("home/", PostsListView.as_view(), name="home"),
]
