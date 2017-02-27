from django.conf.urls import url, include
from django.contrib import admin

from courses import views

urlpatterns = [
    url(r'^solution/', include('solutions.urls')),
    url(r'^task/', include('tasks.urls')),
    url(r'^website/', include('website.urls')),
    url(r'^lecture/', include('lectures.urls')),
    url(r'^course/', include('courses.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]
