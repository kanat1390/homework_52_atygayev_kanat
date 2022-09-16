from todo.models import Todo 
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

def get_all_todos() -> QuerySet:
   return  Todo.objects.all()

def get_todo_by_pk(pk:str or int) -> Todo:
   return get_object_or_404(Todo, pk=pk)
