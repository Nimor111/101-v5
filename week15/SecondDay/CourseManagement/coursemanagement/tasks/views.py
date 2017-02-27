from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Task

from .forms import TaskForm


# Create your views here.
class TaskListView(generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'all_tasks'

    def get_queryset(self):
        """
        Return all tasks
        """
        return Task.objects.all()


class TaskCreateView(generic.CreateView):
    template_name = 'tasks/add_task.html'
    form_class = TaskForm
    success_url = '/'


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs['pk'])
