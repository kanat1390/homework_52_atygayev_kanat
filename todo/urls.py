from unicodedata import name
from django.urls import path
from .views import todo_list, todo_create, todo_update, todo_delete

app_name = 'todo'

urlpatterns = [
    path('', todo_list, name ='todo_list'),
    path('todos/create/', todo_create, name = 'todo_create'),
    path('todos/<int:pk>/update/', todo_update, name='todo_update'),
    path('todos/<int:pk>/delete/', todo_delete, name='todo_delete')
]
