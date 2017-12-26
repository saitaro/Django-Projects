from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    principal = models.CharField(max_length=255)
    location = models.ForeignKey(City)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('basic:detail', kwargs={'pk': self.pk})

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students')
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255)
    continent = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        # managed = True
        # verbose_name = 'City'
        verbose_name_plural = 'Cities'