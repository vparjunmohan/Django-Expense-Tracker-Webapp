from .views import *
from django.urls import  path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', index, name='expenses'),
    path('add-expense/', add_expense, name='add-expenses'),
    path('edit-expense/<int:pk>', expense_edit, name='expense-edit'),
    path('delete-expense/<int:pk>', delete_expense, name='expense-delete'),
    path('search-expenses', csrf_exempt(search_expenses), name='search_expenses'),
]
