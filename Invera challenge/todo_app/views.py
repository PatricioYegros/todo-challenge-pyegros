from django.shortcuts import render

from django.urls import reverse, reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Task, TaskFilter

class TaskListView(ListView):
    model = Task
    template_name = "todo_app/index.html"

class TaskCreate(CreateView):
    model = Task
    fields = [
        "title",
        "description",
        "status"
    ]

    def get_context_data(self):
        context = super(TaskCreate, self).get_context_data()  
        return context
    
    def get_success_url(self):
        return reverse("index")

class TaskUpdate(UpdateView):
    model = Task
    template_name = "todo_app/task_update.html"
    fields = [
        "title",
        "description",
        "status"
    ]

    def get_context_data(self):
        context = super(TaskUpdate, self).get_context_data()
        return context

    def get_success_url(self):
        return reverse("index")


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("index")

#def TaskList(request):
#    filter = TaskFilter(request.GET, queryset=Task.objects.all())
#    return render(request, 'todo_app/task-search.html', {'filter': filter})


def TaskList(request):
    if request.method == "GET":
        request_title = request.GET.get("title")
        request_description = request.GET.get("description")
        request_created_date = request.GET.get("created_date")

        if request_title:
            context = {
                "task_list":Task.objects.filter(title__contains=request_title),
            }

        elif request_description:
            context = {
                "task_list":Task.objects.filter(description__contains=request_description),
            }
        
        elif request_created_date:
            context = {
                "task_list":Task.objects.filter(created_date__date=request_created_date),
            }
            
        else:
            context = {}

    return render(request,'todo_app/task-search.html',context)