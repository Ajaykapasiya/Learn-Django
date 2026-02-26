from django.urls import path,include
from todolist import views

urlpatterns = [
    path('todolist',views.todolist,name="todolist")
]