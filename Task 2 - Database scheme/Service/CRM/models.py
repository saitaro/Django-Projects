from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=127)
    
    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    def service(self):

        # return Skill.objects.filter(masters__employer__name=self.name).distinct()
        return self.masters.all().values_list('skills__name', flat=True).distinct()


class Skill(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Master(models.Model):
    name = models.CharField(max_length=127)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL,
                                 related_name='masters')
    skills = models.ManyToManyField(Skill, related_name='masters')

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    service = models.ForeignKey(Skill, related_name='orders', on_delete=models.CASCADE)
    executor = models.ForeignKey(Master, related_name='orders', null=True, on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(auto_now_add=True)
    execution_date = models.DateTimeField()

    def set_execution_date(self, date):
        self.execution_date = date

    def __str__(self):
        return '{} – {} by {}'.format(str(self.pk), self.service, self.executor)

