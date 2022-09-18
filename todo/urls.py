from unicodedata import name
from django.urls import path
from .views import todo_list, todo_detail, todo_create

app_name = 'todo'

urlpatterns = [
    path('', todo_list, name ='todo_list'),
    path('todos/', todo_detail, name = 'todo_detail'),
    path('todos/create/', todo_create, name = 'todo_create'),
]
