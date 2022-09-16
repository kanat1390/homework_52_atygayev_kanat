from todo.models import Todo 
from django.db.models.query import QuerySet

def get_all_todos() -> QuerySet:
   return  Todo.objects.all()
