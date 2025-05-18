from django.urls import path
from . import views


app_name = 'first_project'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
