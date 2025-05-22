from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('home/', views.about, name='home'),
    path('contacts/', views.contact, name='contacts')
]
