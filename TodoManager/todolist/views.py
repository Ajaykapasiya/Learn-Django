from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def hompage(request):
  
    return render(request, "main.html", {})

def todolist(request):
  
    return render(request, "todolist.html", {})


def contact(request):
  
    return render(request, "contact.html", {})

def about(request):
  
    return render(request, "about.html", {})
