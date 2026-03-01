from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from todolist.models import Task
from todolist.forms import TaskForm

def hompage(request):
  
    return render(request, "main.html", {})


def todolist(request):
    if request.method == "POST":
       form_data = TaskForm(request.POST or None)
       if form_data.is_valid():
        form_data.save()
        return redirect('todolist')
    all_task = Task.objects.all()
    context = {
        'page':'todolist',
        'all_tasks':all_task
    }
    return render(request, "todolist.html",context)


def contact(request):
  
    return render(request, "contact.html", {})

def about(request):
  
    return render(request, "about.html", {})
