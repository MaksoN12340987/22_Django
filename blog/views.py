import logging

<<<<<<< HEAD
from django.urls import reverse, reverse_lazy  # type: ignore
from django.views.generic import (  # type: ignore
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
=======
from django.shortcuts import render  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import DeleteView  # type: ignore
from django.views.generic import (CreateView, DetailView,  # type: ignore
                                  ListView)

from blog.apps import BlogProjectName
>>>>>>> b515b74ecb50180b82f5739d525e6d1da1c0d391

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
    template_name = f"{BlogProjectName.name}/home.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Posts.objects.filter(publication_flag=True)


class PostsDetail(DetailView):
    model = Posts
    template_name = f"{BlogProjectName.name}/post.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        object_post = super().get_object(queryset)
        object_post.number_views += 1
        object_post.save()
        return object_post


class PostsCreate(CreateView):
    model = Posts
<<<<<<< HEAD
    template_name = "blog/create.html"
    form_class = CreatePostForm

    success_url = reverse_lazy("blog:home")


class PostsUpdate(UpdateView):
    model = Posts
    template_name = "blog/update.html"
    context_object_name = "post"
    form_class = UpdatePostForm

    def get_success_url(self):
        return reverse("blog:post", args=[self.kwargs.get("pk")])



class PostsDelete(DeleteView):
    model = Posts
    template_name = "blog/delete.html"
    context_object_name = "post"
=======
    template_name = f"{BlogProjectName.name}/create.html"
    fields = ["title", "content", "number_views"]
>>>>>>> b515b74ecb50180b82f5739d525e6d1da1c0d391
    success_url = reverse_lazy("blog:home")
