from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def calc_approx_duration(self):
        if self.start_date is not None and self.end_date is not None:
            return self.end_date - self.start_date
