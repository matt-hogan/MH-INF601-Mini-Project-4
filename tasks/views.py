from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Task

class IncompleteTasksView(generic.ListView):
    template_name = "tasks/incomplete.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(completed=False).values()


class CompleteTasksView(generic.ListView):
    template_name = "tasks/complete.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(completed=True).values()


def create_task(request):
    """ Add task to databse with provided form values and redirect to the incomplete tasks page """
    Task.objects.create(
        title=request.POST["title"],
        description=request.POST["description"],
        completed=False
    )
    return HttpResponseRedirect(reverse('tasks:index'))


def update_task(request, task_id):
    """ Updates a tasks title and description in the database """
    Task.objects.filter(id=task_id).update(
        title=request.POST["title"],
        description=request.POST["description"],
    )
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def dismiss_task(request, task_id):
    """ Changes a task's status to complete or incomplete """
    task = get_object_or_404(Task, pk=task_id)
    Task.objects.filter(id=task_id).update(
        completed=not task.completed
    )
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

def delete_task(request, task_id):
    """ Deletes a task from the database """
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
