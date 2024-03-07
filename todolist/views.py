from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ToDo
from django.views.decorators.http import require_http_methods
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt


def index(request):
    todos = ToDo.objects.all()
    return render(request, "todoapp/index.html", {'todo_list': todos, 'title': 'Main page'})


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    description = request.POST['description']
    todo = ToDo(title=title, description=description)
    todo.save()
    return redirect('index')


@csrf_exempt
def update(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST.get('title', '')
        todo.description = request.POST.get('description', '')
        todo.save()
        return redirect('index')
    else:
        return render(request, 'todoapp/update.html', {'todo': todo})


def update_button(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
