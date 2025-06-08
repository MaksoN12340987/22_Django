import logging

from django.shortcuts import render  # type: ignore
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView  # type: ignore

from catalog.apps import CatalogProjectConfig

from .models import Category, Product

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


class ProductDeleteView(DeleteView):
    model = Product
    template_name = f"{CatalogProjectConfig.name}/orders.html"
    success_url = reverse_lazy('orders_delite')




def orders(request):
    logger_views.debug(request)
    return render(request, f"{CatalogProjectConfig.name}/orders.html")


def contacts(request):
    logger_views.info(request)
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("box")
        message = request.POST.get("Textarea2")
        logger_views.debug(name, phone, message)

        return render(request, f"{CatalogProjectConfig.name}/response.html")
    else:
        return render(request, f"{CatalogProjectConfig.name}/contacts.html")


# def product(request, product_id):
#     logger_views.debug(request)
#     product = Product.objects.get(id=product_id)
#     context = {
#         'product': product,
#     }
#     return render(request, f"{CatalogProjectConfig.name}/product.html", context)
