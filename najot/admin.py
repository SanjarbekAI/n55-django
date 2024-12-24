from django.contrib import admin

from . import models


@admin.register(models.TeachersModel)
class TeachersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['-name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(models.StudentsModel)
class StudentsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['-name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(models.GroupsModel)
class GroupsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['-name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(models.LessonsModel)
class LessonsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['-name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(models.HomeworksModel)
class HomeworksAdmin(admin.ModelAdmin):
    list_display = ['id', 'info']
    ordering = ['-info']
    list_filter = ['info']
    search_fields = ['info']

