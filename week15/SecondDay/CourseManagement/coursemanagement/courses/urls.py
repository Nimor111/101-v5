from django.conf.urls import url

from . import views


app_name = 'courses'
urlpatterns = [
    url(r'^new/$', views.new, name='new'),
    url(r'^edit/(?P<course_name>[a-zA-Z0-9\-]+)/$',
        views.edit_course, name='edit'),
    url(r'^(?P<course_name>[a-zA-Z0-9\-]+)/$', views.detail_course,
        name='detail'),
]
