from django.db import models
from datetime import datetime

# Create your models here.
class Ticket(models.Model):
    task = models.CharField(max_length=127)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.task
        