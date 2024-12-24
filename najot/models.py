from django.db import models


class TeachersModel(models.Model):
    name = models.CharField(max_length=255)


class StudentsModel(models.Model):
    name = models.CharField(max_length=255)


class GroupsModel(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ManyToManyField(TeachersModel)
    students = models.ManyToManyField(StudentsModel)


class LessonsModel(models.Model):
    name = models.CharField(max_length=255)
    groups = models.ForeignKey(GroupsModel, on_delete=models.PROTECT)


class HomeworksModel(models.Model):
    info = models.TextField()
    lesson = models.OneToOneField(LessonsModel, on_delete=models.CASCADE)
