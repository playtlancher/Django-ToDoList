from django.urls import path
from tasks import views

urlpatterns = [
    path("tasks/", views.taskPage, name="tasks"),
    path("add-task/", views.addTask, name="addTask"),
    path("task/<int:id>", views.task, name="task"),
    path("task/<int:id>/delete", views.deleteTask, name="deleteTask"),
    path("task/<int:id>/edit", views.editTask, name="editTask"),
    path("account", views.taskPage, name="account"),
]
