from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore

from blog.apps import BlogProjectName

from .views import PostsCreate, PostsDelete, PostsDetail, PostsList, PostsUpdate

app_name = BlogProjectName.name

urlpatterns = [
    path("", PostsList.as_view(), name="home"),
    path("<int:pk>/", PostsDetail.as_view(), name="post"),
    path("update/<int:pk>/", PostsUpdate.as_view(), name="update"),
    path("create/", PostsCreate.as_view(), name="create"),
    path("<int:pk>/delete/", PostsDelete.as_view(), name="delete"),
]
