from django.db import models

from courses.models import Course


# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=120)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    @classmethod
    def login(cls, email, password):
        if User.objects.filter(email=email, password=password).exists():
            return User.objects.filter(email=email, password=password)
        else:
            return None


class Student(User):
    course = models.ForeignKey(Course)


class Teacher(User):
    course = models.ForeignKey(Course)
