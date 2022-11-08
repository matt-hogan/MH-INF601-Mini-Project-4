from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("login/", views.signin, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.signout, name="logout"),
]