from django.urls import path  # type: ignore

from catalog.apps import CatalogProjectConfig

from . import views

app_name = CatalogProjectConfig.name

urlpatterns = [
    # path("home/", views.home, name="home"),
    path("catalog/", views.catalog, name="catalog"),
    path("orders/", views.orders, name="orders"),
    path("contacts/", views.contacts, name="contacts"),
    path("response/", views.contacts, name="response"),
    # path("product/<int:product_id>", views.ProductDetailView.as_view(), name="product_detail_view"),
    # path("media/", views.ProductListView.as_view(), name="media"),
    path(
        f"{CatalogProjectConfig.name}/",
        views.contacts,
        name=f"{CatalogProjectConfig.name}",
    ),
    path('home/', views.ProductListView.as_view(), name=f'{CatalogProjectConfig.name}:home'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name=f'{CatalogProjectConfig.name}:product')
]
