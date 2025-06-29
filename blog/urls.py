from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore

from blog.apps import BlogProjectName

from .views import PostsCreate, PostsDetail, PostsList

app_name = BlogProjectName.name

urlpatterns = [
<<<<<<< HEAD
    path("", PostsList.as_view(), name="home"),
    path("<int:pk>/", PostsDetail.as_view(), name="post"),
    path("update/<int:pk>/", PostsUpdate.as_view(), name="update"),
    path("create/", PostsCreate.as_view(), name="create"),
    path("<int:pk>/delete/", PostsDelete.as_view(), name="delete"),
=======
    path("home/", PostsList.as_view(), name="home"),
    path("post/<int:pk>", PostsDetail.as_view(), name="post"),
    path("create/", PostsCreate.as_view(), name="create"),
>>>>>>> b515b74ecb50180b82f5739d525e6d1da1c0d391
]
