from django.contrib import admin
from teams.models import Team, Skill


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


admin.site.register(Team, TeamAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = [
        'language',
    ]


admin.site.register(Skill, SkillAdmin)
