from django.shortcuts import render

def todo_list(request):
    return render(request, 'todo/todo_list.html')
