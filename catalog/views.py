import logging

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
    if 'home' in f'{request}':
        return render(request, f"{CatalogProjectConfig.name}/home.html")


def catalog(request):
    logger_views.debug(request)
    if 'catalog' in f'{request}':
        return render(request, f"{CatalogProjectConfig.name}/catalog.html")


def orders(request):
    logger_views.debug(request)
    if 'orders' in f'{request}':
        return render(request, f"{CatalogProjectConfig.name}/orders.html")


def contacts(request):
    logger_views.debug(request)
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("box")
        message = request.POST.get("floatingTextarea2")
        logger_views.debug(name, phone, message)

        return render(request, f"{CatalogProjectConfig.name}/response.html")
    return render(request, f"{CatalogProjectConfig.name}/contacts.html")
