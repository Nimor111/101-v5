from django.conf.urls import url

from courses import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<course>[A-Za-z]+)/$', views.detail_course, name='detail'),
]
