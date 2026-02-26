from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def todolist(request):
  
    return render(request, "main.html", {})
