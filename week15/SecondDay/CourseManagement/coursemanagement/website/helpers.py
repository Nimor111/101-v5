from courses.models import Course

from .models import User, Student, Teacher


def promote_to_student(user, course_name):
    course = Course.objects.get(name=course_name)

    Student.objects.create(email=user.email, password=user.password,
                           first_name=user.first_name,
                           last_name=user.last_name,
                           course=course)


def promote_to_teacher(user, course_name):
    course = Course.objects.get(name=course_name)

    Teacher.objects.create(email=user.email, password=user.password,
                           first_name=user.first_name,
                           last_name=user.last_name, course=course)
