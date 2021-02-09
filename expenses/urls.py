from .views import *
from django.urls import  path


urlpatterns = [
    path('', index, name='expenses'),
    path('add-expense/', add_expense, name='add-expenses'),
]
