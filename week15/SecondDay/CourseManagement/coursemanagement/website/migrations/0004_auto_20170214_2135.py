# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170210_1652'),
        ('website', '0003_auto_20170214_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='courses.Course'),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='course',
        ),
        migrations.AddField(
            model_name='teacher',
            name='course',
            field=models.ManyToManyField(to='courses.Course'),
        ),
    ]
