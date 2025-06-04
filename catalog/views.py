import logging

from .models import Product
from catalog.apps import CatalogProjectConfig

logger_views = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views.addHandler(file_handler)
logger_views.setLevel(logging.INFO)


from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    logger_views.debug(request)
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, f"{CatalogProjectConfig.name}/home.html", context)


def catalog(request):
    logger_views.debug(request)
    return render(request, f"{CatalogProjectConfig.name}/catalog.html")


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

def product(request, product_id):
    logger_views.debug(request)
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, f"{CatalogProjectConfig.name}/product.html", context)
