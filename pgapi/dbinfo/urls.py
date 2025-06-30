from django.urls import path
from .views import list_tables, create_user

urlpatterns = [
    path('tables/', list_tables, name='list_tables'),
    path('users/', create_user, name='create_user'),
]
