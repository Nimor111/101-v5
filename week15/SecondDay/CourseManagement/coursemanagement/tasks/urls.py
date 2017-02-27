from django.conf.urls import url

from . import views

app_name = "tasks"
urlpatterns = [
    url(r'^$', views.TaskListView.as_view(), name='index'),
    url(r'^add$', views.TaskCreateView.as_view(), name='add_task'),
    url(r'^(?P<pk>[0-9]+)', views.TaskDetailView.as_view(), name='t_detail'),
]
