import logging

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from blog.apps import BlogConfig

from .forms import CreatePostForm, UpdatePostForm
from .models import Posts

logger_views = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views.addHandler(file_handler)
logger_views.setLevel(logging.INFO)


class PostsList(ListView):
    model = Posts
    template_name = "blog/home.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Posts.objects.filter(publication_flag=True)


class PostsDetail(DetailView):
    model = Posts
    template_name = "blog/post.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        object_post = super().get_object(queryset)
        object_post.number_views += 1  # type: ignore
        object_post.save()
        return object_post


class PostsCreate(CreateView):
    model = Posts
    template_name = "blog/create.html"
    fields = ["title", "content", "number_views"]
    success_url = reverse_lazy("blog:home")


class PostsUpdate(UpdateView):
    model = Posts
    template_name = "blog/create.html"
    fields = ["title", "content", "number_views"]
    success_url = reverse_lazy("blog:home")


class PostsDelete(DeleteView):
    model = Posts
    template_name = "blog/create.html"
    fields = ["title", "content", "number_views"]
    success_url = reverse_lazy("blog:home")
