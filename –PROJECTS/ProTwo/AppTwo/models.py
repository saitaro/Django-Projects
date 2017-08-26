from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20, unique=False)
    last_name = models.CharField(max_length=40, unique=False)

    def __str__(self):
        return self.first_name +' '+ self.last_name

class Mail(models.Model):
    owner = models.ForeignKey(User)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.url