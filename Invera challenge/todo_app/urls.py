# todo_list/todo_app/urls.py
from django.urls import path
from todo_app import views
from users import views as viewsusers

urlpatterns = [
    path("", viewsusers.sign_in, name="login"),
    path("task/", views.TaskListView.as_view(), name="index"),
    # CRUD patterns for Tasks
    path("task/add/",views.TaskCreate.as_view(),name="task-add"),
    path("task/<int:pk>/",views.TaskUpdate.as_view(),name="task-update"),
    path("task/<int:pk>/delete/",views.TaskDelete.as_view(),name="task-delete"),
    path("task/search/",views.TaskList,name="task-search")
]   