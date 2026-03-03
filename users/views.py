from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        pass
    else:
        pass
    register_form  = UserCreationForm() 
    return render(request, 'register.html',{'register_form':register_form})