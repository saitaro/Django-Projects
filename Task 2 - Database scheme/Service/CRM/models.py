from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=127, unique=True)
    
    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    def services(self):
        return Skill.objects.filter(masters__employer__name=self.name).distinct()


class Skill(models.Model):
    name = models.CharField(max_length=127, unique=True)

    def __str__(self):
        return self.name


class Master(models.Model):
    name = models.CharField(max_length=127, unique=True)
    employer = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL,
                                 related_name='employees')
    skill = models.ManyToManyField(Skill, related_name='masters', null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Skill, on_delete=models.CASCADE)
    executor = models.ForeignKey(Master, null=True, on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(auto_now_add=True)
    execution_date = models.DateTimeField()

    def set_execution_date(self, date):
        self.execution_date = date

    def __str__(self):
        return '{} – {} by {}'.format(str(self.pk), self.service, self.executor)

