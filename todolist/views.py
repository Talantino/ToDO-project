from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo


def index(request):
    todos = ToDo.objects.all
    return render(request, "todoapp/index.html", {'todolist':todos, 'title': 'Main page'})
git
