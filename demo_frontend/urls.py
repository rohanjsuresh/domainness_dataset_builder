from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'add_entry/', views.add_entry, name='add_entry'),
    path(r'skip_entry/', views.skip_entry, name='skip_entry'),
    # path(r'add_user/', views.add_user, name='add_user'),
]
