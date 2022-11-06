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


def get_task(id):
    """ Returns a single task from the database """
    return Task.objects.get(id=id)