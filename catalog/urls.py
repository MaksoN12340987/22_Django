from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.ProductListView.as_view(), name="home"),
    path("catalog/", views.ProductCategoriesListView.as_view(), name="catalog"),
    path("product/<int:pk>/", views.ProductView.as_view(), name="product"),
    path("orders/", views.OrdersView.as_view(), name="orders"),
    path("delete/<int:pk>/", views.OrdersDelete.as_view(), name="delete"),
    path("create/", views.CreateProduct.as_view(), name="create"),
]
