import logging

from django.urls import reverse_lazy, reverse  # type: ignore
from django.views.generic import (CreateView, DetailView,  # type: ignore
                                  ListView, UpdateView, DeleteView)

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
        # Получаем только активные объекты
        return Posts.objects.filter(publication_flag=True)
        


class PostsDetail(DetailView):
    model = Posts
    template_name = "blog/post.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        object_post = super().get_object(queryset)
        object_post.number_views += 1
        object_post.save()
        return object_post



class PostsCreate(CreateView):
    model = Posts
    template_name = "blog/create.html"
    fields = ["title", "content", "number_views"]

    success_url = reverse_lazy('blog:home')



class PostsUpdate(UpdateView):
    model = Posts
    template_name = "blog/update.html"
    context_object_name = "post"
    fields = ["title", "content", "publication_flag", "preview"]
    
    def get_success_url(self):
        return reverse('blog:post', args=[self.kwargs.get('pk')])
# end_metro.jpg


class PostsDelete(DeleteView):
    model = Posts
    template_name = "blog/delite.html"
    context_object_name = "post"
    
    def get_success_url(self):
        return reverse('blog:home')
