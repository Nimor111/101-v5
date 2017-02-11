from django.shortcuts import render, get_object_or_404

from django.http import Http404

from courses.models import Course
from .models import Lecture


# Create your views here.
def index(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)

    return render(request, 'lectures/index.html', locals())


def new(request):
    lecture_created = False
    courses = Course.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        week = request.POST.get('week')
        url = request.POST.get('url')
        course = get_object_or_404(Course, pk=request.POST.get('dropdown'))
        lecture = Lecture.objects.create(name=name, week=week, url=url,
                                         course=course)
        lecture_created = True
    return render(request, 'lectures/new.html', locals())


def edit(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    courses = Course.objects.all()
    lecture_edited = False

    if request.method == 'POST':
        if request.POST.get('dropdown'):
            course = get_object_or_404(Course, pk=request.POST.get('dropdown'))
            lecture.course = course
            lecture_edited = True
        attrs = [attr for attr in list(lecture.__dict__.keys())
                 if attr != '_state' or attr != 'id']
        for attr in attrs:
            if request.POST.get(attr):
                setattr(lecture, attr, request.POST.get(attr))
                lecture_edited = True

        lecture.save()

    return render(request, 'lectures/edit_lecture.html', locals())
