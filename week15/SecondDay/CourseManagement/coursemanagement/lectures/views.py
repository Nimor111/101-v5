from django.shortcuts import render, get_object_or_404, redirect

from django.http import Http404

from website.decorators import login_required

from courses.models import Course
from .models import Lecture
from website.models import Student, Teacher


# Create your views here.
@login_required(redirect_url='/website/login')
def index(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    perm = None
    teacher = student = False

    if request.session.get('email'):
        try:
            perm = Teacher.objects.get(email=request.session.get('email'))
            teacher = True
        except Teacher.DoesNotExist:
            perm = Student.objects.get(email=request.session.get('email'))
            student = True
    if request.method == 'POST':
        if request.POST.get('~lecture'):
            return redirect('/lecture/edit/{}'.format(lecture.id))

    return render(request, 'lectures/index.html', locals())


def new(request):
    lecture_created = False
    courses = Course.objects.all()
    if request.method == 'POST':
        if request.POST.get('home'):
            return redirect('/')

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
        if request.POST.get('home'):
            return redirect('/')

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
