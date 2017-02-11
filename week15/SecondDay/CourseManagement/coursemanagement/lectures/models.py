from django.db import models

from courses.models import Course


# Create your models here.
class Lecture(models.Model):
    name = models.CharField(max_length=40)
    week = models.IntegerField()
    course = models.ForeignKey(Course)
    url = models.TextField()
