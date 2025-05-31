from django.urls import path

from catalog.apps import CatalogProjectConfig

from . import views

app_name = CatalogProjectConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path("catalog/", views.home, name="catalog"),
    path("orders/", views.home, name="orders"),
    path("contacts/", views.contacts, name="contacts"),
    path("response/", views.home, name="response"),
    path(
        f"{CatalogProjectConfig.name}/",
        views.contacts,
        name=f"{CatalogProjectConfig.name}",
    ),
]
