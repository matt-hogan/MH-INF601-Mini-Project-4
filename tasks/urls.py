from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.IncompleteTasksView.as_view(), name="index"),
    path("completed/", views.CompleteTasksView.as_view(), name="completed"),
    # path("create/", , name="create"),
    # path("<int:pk>/update/", , name="update"),
    # path("<int:pk>/dismiss/", , name="dismiss"),
    # path("<int:pk>/delete/", , name="delete"),
]