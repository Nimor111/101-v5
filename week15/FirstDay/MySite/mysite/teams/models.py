from django.db import models


# Create your models here
class Skill(models.Model):
    language = models.CharField(max_length=30)


class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.ForeignKey(Skill, blank=True, null=True)
