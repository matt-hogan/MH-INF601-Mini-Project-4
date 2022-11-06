from django.urls import path

from . import views

urlpatterns = [
    path("", views.TasksView.as_view(), name="index"),
    # path("completed/", , name="completed"),
    # path("create/", , name="create"),
    # path("<int:pk>/update/", , name="update"),
    # path("<int:pk>/dismiss/", , name="dismiss"),
    # path("<int:pk>/delete/", , name="delete"),
]