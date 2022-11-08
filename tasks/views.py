from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Task

class IncompleteTasksView(LoginRequiredMixin, generic.ListView):
    template_name = "tasks/incomplete.html"
    context_object_name = "tasks"

    def get_queryset(self):
        # TODO: Display welcome page if not logged in
        if self.request.user.is_superuser:
            return Task.objects.filter(completed=False).values()
        return Task.objects.filter(completed=False, user=self.request.user).values()


class CompleteTasksView(LoginRequiredMixin, generic.ListView):
    template_name = "tasks/complete.html"
    context_object_name = "tasks"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.filter(completed=False).values()
        return Task.objects.filter(completed=False, user=self.request.user).values()


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
