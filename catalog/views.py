import logging

from catalog.apps import CatalogProjectConfig


logger_views = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_views.addHandler(file_handler)
logger_views.setLevel(logging.INFO)



from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    logger_views.debug(request)
    return render(request, f'{CatalogProjectConfig.name}/home.html')

def contacts(request):
    logger_views.debug(request)
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        
        return render(request, f'{CatalogProjectConfig.name}/response.html')
    return render(request, f'{CatalogProjectConfig.name}/contacts.html')
