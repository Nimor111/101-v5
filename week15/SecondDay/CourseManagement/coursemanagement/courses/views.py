from django.shortcuts import render

from .models import Course


# Create your views here.
def index(request):
    return render(request, 'courses/index.html', locals())


def new(request):
    course_created = False
    name = request.POST.get('name', False)
    description = request.POST.get('description', False)
    start_date = request.POST.get('start_date', False)
    end_date = request.POST.get('end_date', False)

    Course.objects.create(name=name, description=description,
                          start_date=start_date, end_date=end_date)
    course_created = True

    return render(request, 'courses/new_course.html', locals())


def detail_course(request, *args, **kwargs):
    return render(request, 'courses/course_detail.html', locals())
