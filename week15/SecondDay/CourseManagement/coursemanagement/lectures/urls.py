from django.conf.urls import url

from . import views

app_name = "lectures"
urlpatterns = [
    url(r'^edit/(?P<lecture_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^(?P<lecture_id>[0-9]+)/$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
]
