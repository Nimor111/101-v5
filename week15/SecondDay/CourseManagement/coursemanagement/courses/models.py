from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
