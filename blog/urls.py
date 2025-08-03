from django.urls import path

from blog.apps import BlogConfig

from .views import PostsCreate, PostsDetail, PostsList, PostsUpdate, PostsDelete

app_name = BlogConfig.name

urlpatterns = [
    path("", PostsList.as_view(), name="home"),
    path("<int:pk>/", PostsDetail.as_view(), name="post"),
    path("update/<int:pk>/", PostsUpdate.as_view(), name="update"),
    path("create/", PostsCreate.as_view(), name="create"),
    path("<int:pk>/delete/", PostsDelete.as_view(), name="delete"),
]
