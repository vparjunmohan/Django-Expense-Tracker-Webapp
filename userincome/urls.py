from .views import *
from django.urls import  path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', index, name='income'),
    path('add-income/', add_income, name='add-income'),
    path('edit-income/<int:pk>', income_edit, name='income-edit'),
    path('delete-income/<int:pk>', delete_income, name='income-delete'),
    path('search-income', csrf_exempt(search_income), name='search_income'),
]
