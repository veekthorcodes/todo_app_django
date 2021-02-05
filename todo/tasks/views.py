from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by('-id')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/home.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form':form, 'task':task}
    return render(request, 'tasks/update.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')

    context = {'task':task}
    return render(request, 'tasks/delete.html', context)
