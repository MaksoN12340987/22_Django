from django.urls import path  # type: ignore

from catalog.apps import CatalogProjectConfig

from . import views

app_name = CatalogProjectConfig.name

urlpatterns = [
    path("home/", views.ProductListView.as_view(), name="home"),
    
    path("catalog/", views.ProductCategoriesListView.as_view(), name="catalog"),
    path("product/<int:pk>", views.ProductDetailView.as_view(), name="product"),
    
    path("orders/", views.OrdersView.as_view(), name="orders"),
    path("orders_delite/<int:pk>", views.OrdersDelete.as_view(), name="orders_delite"),
    
    path("contacts/", views.CreateUser.as_view(), name="contacts"),
    path("users/", views.UsersView.as_view(), name="users"),
]
