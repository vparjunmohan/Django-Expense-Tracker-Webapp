from .views import *
from django.urls import  path


urlpatterns = [
    path('', index, name='expenses'),
    path('add-expense/', add_expense, name='add-expenses'),
    path('edit-expense/<int:pk>', expense_edit, name='expense-edit'),
    path('delete-expense/<int:pk>', delete_expense, name='expense-delete'),
]
