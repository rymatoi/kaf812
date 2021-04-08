from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Discipline(models.Model):
    name = models.CharField(max_length=100)


class Professors(models.Model):
    name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return f'/professor/{self.pk}/'


class Groups(models.Model):
    name = models.CharField(max_length=20, null=True)
    discipline = models.ForeignKey(
        Discipline, on_delete=models.CASCADE, related_name='discipline', null=True)
    lector = models.ForeignKey(
        Professors, on_delete=models.CASCADE, related_name='lector', null=True)
    seminarist = models.ForeignKey(
        Professors, on_delete=models.CASCADE, related_name='seminarist', null=True)

    def get_absolute_url(self):
        return f'/group/{self.pk}/'


class UsersXProfessors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professors, on_delete=models.CASCADE)


class Students(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(
        Groups, on_delete=models.CASCADE, null=True)
    z1 = models.CharField(max_length=1, default='0')
    z2 = models.CharField(max_length=1, default='0')
    z3 = models.CharField(max_length=1, default='0')
    z4 = models.CharField(max_length=1, default='0')
    z5 = models.CharField(max_length=1, default='0')
    z6 = models.CharField(max_length=1, default='0')
    z7 = models.CharField(max_length=1, default='0')
    z8 = models.CharField(max_length=1, default='0')
    z9 = models.CharField(max_length=1, default='0')
    z10 = models.CharField(max_length=1, default='0')
    sum = models.CharField(max_length=3, default='0')


class ProfessorTypes(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return f'/groups/{self.pk}/'
