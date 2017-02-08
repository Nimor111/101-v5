from django.shortcuts import render

from teams.models import Team

from django.http import HttpResponse


def index(request):
    teams = Team.objects.all()
    return render(request, 'teams/index.html', locals())
