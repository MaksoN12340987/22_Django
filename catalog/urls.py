from django.urls import path
from . import views
from catalog.apps import CatalogProjectConfig


app_name = CatalogProjectConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path(f'{CatalogProjectConfig.name}/', views.contacts, name=f'{CatalogProjectConfig.name}')
]
