from django.urls import path
from .views import todo_list, todo_detail

app_name = 'todo'

urlpatterns = [
    path('', todo_list, name ='todo_list'),
    path('todos/', todo_detail, name = 'todo_detail')
]
