import logging

from django.shortcuts import render  # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views.generic import ( # type: ignore
    CreateView,
    DeleteView,  # type: ignore
    DetailView,
    ListView,
)

from catalog.apps import CatalogProjectConfig

from .models import Category, Product, Users

logger_views = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views.addHandler(file_handler)
logger_views.setLevel(logging.INFO)


class ProductListView(ListView):
    model = Product
    template_name = f"{CatalogProjectConfig.name}/home.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = f"{CatalogProjectConfig.name}/product.html"
    context_object_name = "product"


class ProductCategoriesListView(ListView):
    model = Product
    template_name = f"{CatalogProjectConfig.name}/catalog.html"
    context_object_name = "products"


class OrdersView(ListView):
    model = Product
    template_name = f"{CatalogProjectConfig.name}/orders.html"
    context_object_name = "products"


class OrdersDelete(DeleteView):
    model = Product
    template_name = f"{CatalogProjectConfig.name}/orders_delite.html"
    success_url = reverse_lazy("catalog:orders")


class CreateUser(CreateView):
    model = Users
    fields = ["name", "surname", "birthday"]
    template_name = f"{CatalogProjectConfig.name}/contacts.html"
    success_url = reverse_lazy("catalog:users")


class UsersView(ListView):
    model = Users
    template_name = f"{CatalogProjectConfig.name}/users.html"
    context_object_name = "users"
