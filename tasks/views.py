from django.shortcuts import render, redirect

from tasks.forms import AddTaskForm
from tasks.models import Task




def taskPage(request):
    tasks = Task.objects.filter(userId=request.user.id)
    context = {'tasks': tasks}
    if request.method == 'GET':
        return render(request, 'tasks/tasks.html', context)
    return render(request, 'tasks/tasks.html')
def task(request,id):
    task = Task.objects.get(id=id)
    context = {'task': task}
    if request.method == 'GET':
        return render(request, 'tasks/task.html', context)

def addTask(request):
    form = AddTaskForm()
    context = {"form":form}
    if request.method == 'GET':
        return render(request, 'tasks/addTaskForm.html', context)
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.userId = request.user
            task.save()
            context["message"] = "Task added successfully"
        return render(request, 'tasks/addTaskForm.html',context)
    return render(request, 'tasks/addTaskForm.html')
def deleteTask(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("tasks")
def editTask(request,id):
    task = Task.objects.get(id=id)
    form = AddTaskForm(initial={"name":task.name,"description":task.description})
    context = {"form":form,"id":task.id}
    if request.method == 'GET':
        return render(request, 'tasks/editTaskForm.html', context)
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task.name = form.cleaned_data["name"]
            task.description = form.cleaned_data["description"]
            task.save()
            return redirect("tasks")
