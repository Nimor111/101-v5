from django.conf.urls import url

from . import views

app_name = "solutions"
urlpatterns = [
    url(r'^course/(?P<pk>[0-9]+)/new/', views.SolutionCreateView.as_view(),
        name='add_sol'),
]
