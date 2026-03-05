from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path("register/", user_views.register,name="register"),
  path("login/", auth_views.LoginView.as_view(),name="login")

] 