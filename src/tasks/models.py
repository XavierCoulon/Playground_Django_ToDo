from django.db import models
from django.conf import settings


class List(models.Model):
	name = models.CharField(max_length=20, blank=False)
	user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")

	def __str__(self):
		return self.name


class Status(models.Model):
	name = models.CharField(max_length=20, blank=False)

	def __str__(self):
		return self.name


class Task(models.Model):
	list = models.ForeignKey(to='tasks.List', on_delete=models.CASCADE, related_name='list', blank=False)
	status = models.ForeignKey(to='tasks.Status', on_delete=models.CASCADE, related_name='status', blank=False)
	title = models.CharField(max_length=20, blank=False)
	details = models.TextField(max_length=125)
	due_date = models.DateField(null=True, blank=True)
	favorite = models.BooleanField(null=True, blank=True)

	def __str__(self):
		return self.title
