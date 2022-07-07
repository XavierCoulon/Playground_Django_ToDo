from django.db import models
from django.conf import settings


class List(models.Model):
	name = models.CharField(max_length=20, blank=False)
	user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")

	def __str__(self):
		return self.name


class Task(models.Model):
	list = models.ForeignKey(to='tasks.List', on_delete=models.CASCADE, related_name='list', blank=False)
	closed = models.BooleanField(blank=False, default=False)
	title = models.CharField(max_length=20, blank=False)
	details = models.TextField(max_length=125, blank=True)
	due_date = models.DateField(null=True, blank=True)
	favorite = models.BooleanField(null=True, blank=True)

	def __str__(self):
		return self.title
