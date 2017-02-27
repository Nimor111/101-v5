from django.db import models

from courses.models import Course


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(default="")
    course = models.ForeignKey(Course, blank=True, null=True)
