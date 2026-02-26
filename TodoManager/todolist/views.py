from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def todolist(request):
    data = {
        "name":"Ram",
        "loction":"kise ko ni pta ",
    }
    return JsonResponse(data)
