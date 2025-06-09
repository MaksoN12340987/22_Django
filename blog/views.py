import logging

from django.shortcuts import render  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import (  # type: ignore
    CreateView,
    DeleteView,  # type: ignore
    DetailView,
    ListView,
)

from blog.apps import BlogProjectName
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
    template_name = f"{BlogProjectName.name}/home.html"
    context_object_name = "posts"


class PostsDetail(DetailView):
    model = Posts
    template_name = f"{BlogProjectName.name}/post.html"
    context_object_name = "post"


class PostsCreate(CreateView):
    model = Posts
    template_name = f"{BlogProjectName.name}/create.html"
    fields = ['title', 'content', 'number_views']
    success_url = reverse_lazy('blog:home')
