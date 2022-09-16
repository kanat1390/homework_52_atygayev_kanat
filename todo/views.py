from django.shortcuts import render
from todo.services import todo_services

def todo_list(request):
    todo_list = todo_services.get_all_todos()
    context = {
        'todo_list':todo_list,
    }
    return render(request, 'todo/todo_list.html', context)
