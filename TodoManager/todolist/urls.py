from django.urls import path,include
from todolist import views

urlpatterns = [
    path('',views.todolist,name="homepage"),
    path('todolist',views.todolist,name="todolist"),
    path('contact',views.todolist,name="todolist"),
    path('about',views.todolist,name="todolist"), 
]