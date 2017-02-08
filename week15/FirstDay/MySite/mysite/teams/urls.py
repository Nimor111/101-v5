from django.conf.urls import url

from teams import views

urlpatterns = [
    url(r'^index/$', views.index, name='teamindex'),
]
