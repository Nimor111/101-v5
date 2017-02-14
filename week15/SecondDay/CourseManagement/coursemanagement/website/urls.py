from django.conf.urls import url, include

from . import views

app_name = 'website'
urlpatterns = [
    # url(r'^course/', include('courses.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^profile/$', views.profile, name='profile'),
]
