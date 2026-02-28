from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from todolist.models import Task

def hompage(request):
  
    return render(request, "main.html", {})

def todolist(request):
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
