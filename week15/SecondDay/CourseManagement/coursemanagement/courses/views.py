from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from django.http import HttpResponseRedirect

from .models import Course
from lectures.models import Lecture


# Create your views here.
def index(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        if request.POST.get('RegButton'):
            return redirect('website/register')
        else:
            return redirect('website/login')

    return render(request, 'courses/index.html', locals())


def new(request):
    course_created = False
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        Course.objects.create(name=name, description=description,
                              start_date=start_date, end_date=end_date)
        course_created = True

    return render(request, 'courses/new_course.html', locals())


def detail_course(request, course_name):
    course = get_object_or_404(Course, name=course_name)

    lectures = list(course.lecture_set.all())

    return render(request, 'courses/course_detail.html', locals())


def edit_course(request, course_name, *args, **kwargs):
    course = get_object_or_404(Course, name=course_name)
    if request.method == 'POST':
        attrs = [attr for attr in list(course.__dict__.keys())
                 if attr != '_state' and attr != 'id']
        course_edited = False

        for attr in attrs:
            if request.POST.get(attr):
                setattr(course, attr, request.POST[attr])
                course_edited = True
        course.save()
    return render(request, 'courses/edit_course.html', locals())

    # kwargs={'course': course}))
