from django.urls import path

from catalog.apps import CatalogProjectConfig

from . import views

app_name = CatalogProjectConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path("catalog/", views.catalog, name="catalog"),
    path("orders/", views.orders, name="orders"),
    path("contacts/", views.contacts, name="contacts"),
    path("response/", views.contacts, name="response"),
    path(
        f"{CatalogProjectConfig.name}/",
        views.contacts,
        name=f"{CatalogProjectConfig.name}",
    ),
]
