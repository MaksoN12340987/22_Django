from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore

from blog.apps import BlogProjectName

from .views import PostsCreate, PostsDetail, PostsList

app_name = BlogProjectName.name

urlpatterns = [
    path("home/", PostsList.as_view(), name="home"),
    path("post/<int:pk>", PostsDetail.as_view(), name="post"),
    path("create/", PostsCreate.as_view(), name="create"),
]
