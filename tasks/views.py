from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Task

class TasksView(generic.ListView):
    template_name = "tasks/incomplete.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all()


