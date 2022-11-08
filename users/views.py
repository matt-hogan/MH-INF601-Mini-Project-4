from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def signin(request):
    """ Displays the login form and signs a user in """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login user in it exists and redirect to the home page
            login(request, user)
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, "users/login.html", {
                "messages": ["Invalid username or password"],
            })
    return render(request, "users/login.html")

def register(request):
    """ Displays a registration form. Creates a user and signs them in """
    if request.method == "POST":
        # Creates a group if needed and adds the user to the group with permissions to edit tasks
        group, created = Group.objects.get_or_create(name="standard_user")
        if created:
            group.permissions.set([
                Permission.objects.get(codename='add_task'),
                Permission.objects.get(codename='view_task'),
                Permission.objects.get(codename='change_task'),
                Permission.objects.get(codename='delete_task'),
            ])
        try:
            user = User.objects.create_user(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                username=request.POST["username"],
                password=request.POST["password"]
            )
            user.groups.add(group)
            login(request, user)
            return HttpResponseRedirect(reverse('tasks:index'))
        except Exception as exc:
            return render(request, "users/register.html", {
                "messages": ["That username already exists"],
                "first_name": request.POST["first_name"],
                "last_name": request.POST["last_name"],
                "email": request.POST["email"],
                "username": request.POST["username"],
                "password": request.POST["password"],
            })
    return render(request, "users/register.html")



def signout(request):
    """ Logs out a user and redirects to the home page """
    logout(request)
    return HttpResponseRedirect(reverse('tasks:index'))