from django.shortcuts import render
from django.views import generic

from .models import Task
from courses.models import Course

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


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = 'tasks/edit_task.html'
    form_class = TaskForm

    def get_success_url(self):
        return '/task/{}'.format(self.kwargs['pk'])


class TaskCourseListView(generic.ListView):
    template_name = 'tasks/course_tasks.html'
    context_object_name = 'course_tasks'

    def get_queryset(self):
        """
        Return tasks for a course.
        """
        return Task.objects.filter(course=Course.
                                   objects.get(pk=self.kwargs['pk']))
        # import ipdb; ipdb.set_trace()

    def get_context_data(self, **kwargs):
        context = super(TaskCourseListView, self).get_context_data(**kwargs)
        course = Course.objects.get(pk=self.kwargs['pk'])
        context['course'] = course
        return context
