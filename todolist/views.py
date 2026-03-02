from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages 

def hompage(request):
  
    return render(request, "main.html", {})


def todolist(request):
    if request.method == "POST":
       form_data = TaskForm(request.POST or None)
       if form_data.is_valid():
        form_data.save()
        messages.success(request,"Task added successfully!")
        return redirect('todolist')
       messages.error(request,"Something Went Wrong!")
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

def delete(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    task_obj.delete()
    messages.success(request,f"Task {task_obj} is deleted!")
    return redirect("todolist")


def edit(request,task_id):
    task_obj = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form_data=TaskForm(request.POST or None,instance=task_obj)
        if form_data.is_valid():
         form_data.save()
         messages.success(request,"Task Updated!")
         return redirect('todolist')
    else:   
     context = {
        'task_obj': task_obj
        
     }
    return render(request, "edit.html",context)


def complete(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    task_obj.is_completed = True
    task_obj.save()
    messages.success(request,"Task is completed!")
    return redirect('todolist')


def pending(request, task_id):
    task_obj=Task.objects.get(id=task_id)
    task_obj.is_completed = False
    task_obj.save()
    messages.success(request,"Task is completed!")
    return redirect('todolist')

    