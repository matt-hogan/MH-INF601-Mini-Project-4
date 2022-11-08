from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Task


def incomplete_tasks(request):
    """ Displays a users incomplete tasks if logged else otherwise displays the welcome page """
    if request.user.is_authenticated:
        if request.user.is_superuser:
            tasks = Task.objects.filter(completed=False).values()
        else:
            tasks = Task.objects.filter(completed=False, user=request.user).values()
        return render(request, "tasks/incomplete.html", {"tasks": tasks})
    return render(request, "tasks/welcome.html")


@login_required
def complete_tasks(request):
    """ Displays completed tasks to the curretn logged in user """
    if request.user.is_superuser:
        tasks = Task.objects.filter(completed=True).values()
    else:
        tasks = Task.objects.filter(completed=True, user=request.user).values()
    return render(request, "tasks/complete.html", {"tasks": tasks})


@login_required
def create_task(request):
    """ Add task to database with provided form values and redirect to the incomplete tasks page """
    Task.objects.create(
        title=request.POST["title"],
        description=request.POST["description"],
        completed=False,
        user=request.user
    )
    return HttpResponseRedirect(reverse('tasks:index'))


@login_required
def update_task(request, task_id):
    """ Updates a tasks title and description in the database """
    try:
        Task.objects.filter(id=task_id).update(
            title=request.POST["title"],
            description=request.POST["description"],
        )
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    except:
        return HttpResponseRedirect(reverse('tasks:index'))


@login_required
def dismiss_task(request, task_id):
    """ Changes a task's status to complete or incomplete """
    try:
        task = get_object_or_404(Task, pk=task_id)
        Task.objects.filter(id=task_id).update(
            completed=not task.completed
        )
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    except:
        return HttpResponseRedirect(reverse('tasks:index'))


@login_required
def delete_task(request, task_id):
    """ Deletes a task from the database """
    try:
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    except:
        return HttpResponseRedirect(reverse('tasks:index'))
