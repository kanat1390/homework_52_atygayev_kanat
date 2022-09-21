from audioop import reverse
from django.shortcuts import render, redirect, reverse
from todo.services import todo_services
from todo.utils import todo_utils
from .forms import TodoForm

def todo_list(request):
    todo_list = todo_services.get_all_todos()
    context = {
        'todo_list':todo_list,
    }
    return render(request, 'todo/todo_list.html', context)


def todo_create(request):
    if request.method == 'POST':
        todo = {
            'description': request.POST.get('description'),
            'status': request.POST.get('status'),
            'date': todo_utils.check_form_date_field(request.POST.get('date'))
        }
        todo_services.create_todo_task(todo)
        return redirect('todo:todo_list')
    statuses = todo_services.get_status_choices()
    context = {
        'statuses': statuses
    }
    return render(request, 'todo/todo_create.html', context)

def todo_update(request, pk):
    todo = todo_services.get_todo_by_pk(pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect(reverse('todo:todo_detail', kwargs={'pk':todo.pk}))

    statuses = todo_services.get_status_choices()
    context = {
        'todo': todo,
        'statuses': statuses,
    }
    return render(request, 'todo/todo_update.html', context)

def todo_delete(request, pk):
    todo = todo_services.get_todo_by_pk(pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:todo_list')
    context = {
        'todo': todo, 
    }
    return render(request, 'todo/todo_delete.html', context)

def todo_detail(request, pk):
    todo = todo_services.get_todo_by_pk(pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todo/todo_detail.html', context)
    
    
