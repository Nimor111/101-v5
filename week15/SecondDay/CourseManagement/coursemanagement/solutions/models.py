from django.db import models

from tasks.models import Task
from website.models import Student


# Create your models here.
class Solution(models.Model):
    date = models.DateTimeField()
    url = models.CharField(max_length=100)
    task = models.ForeignKey(Task)
    student = models.ForeignKey(Student)
