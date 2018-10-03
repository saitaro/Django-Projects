from django.db import models


class Note(models.Model):
	name = models.CharField(max_length=64)
	body = models.TextField()
	publish = models.DateField(auto_now=True, auto_now_add=False)

	def __str__(self):
  		return self.name
