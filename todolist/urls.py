from django.urls import path,include
from todolist import views

urlpatterns = [
    path('',views.hompage,name="homepage"),
    path('todolist/',views.todolist,name="todolist"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"), 
] 