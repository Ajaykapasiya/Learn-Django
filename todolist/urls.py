from django.urls import path,include
from todolist import views

urlpatterns = [
    path('',views.hompage,name="homepage"),
    path('todolist/',views.todolist,name="todolist"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('delete/<task_id>',views.delete,name="delete"),
    path('edit/<task_id>',views.edit,name="edit"),
    path('complete/<task_id>',views.complete,name="complete")

] 