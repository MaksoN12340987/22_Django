import logging

from django.urls import reverse_lazy  # type: ignore
from django.views.generic import CreateView, DetailView, ListView, DeleteView  # type: ignore

from .models import Product
from .forms import ContactForm

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
    template_name = "catalog/home.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"


class ProductCategoriesListView(ListView):
    model = Product
    template_name = "catalog/catalog.html"
    context_object_name = "products"


class OrdersView(ListView):
    model = Product
    template_name = "catalog/orders.html"
    context_object_name = "products"


class OrdersDelete(DeleteView):
    model = Product
    template_name = "catalog/orders_delite.html"
    success_url = reverse_lazy("catalog:orders")


class CreateProduct(CreateView):
    model = Product
    form_class = ContactForm
    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("catalog:catalog")


# class UsersView(ListView):
#     model = Users
#     template_name = f"{CatalogProjectConfig.name}/users.html"
#     context_object_name = "users"
