from django.shortcuts import render
from django.shortcuts import get_object_or_404
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


def get_task(id):
    """ Returns a single task from the database """
    return Task.objects.get(id=id)