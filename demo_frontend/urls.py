from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'add_entry/', views.add_entry, name='add_entry'),
]