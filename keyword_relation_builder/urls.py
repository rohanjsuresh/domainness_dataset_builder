from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='keyword_relation_home'),
    path(r'add_entry/', views.add_entry, name='add_entry'),
    path(r'skip_entry/', views.skip_entry, name='skip_entry'),
]