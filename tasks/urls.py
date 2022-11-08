from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.incomplete_tasks, name="index"),
    path("completed/", views.complete_tasks, name="completed"),
    path("create/", views.create_task, name="create"),
    path("<int:task_id>/update/", views.update_task, name="update"),
    path("<int:task_id>/dismiss/", views.dismiss_task, name="dismiss"),
    path("<int:task_id>/delete/", views.delete_task, name="delete"),
]