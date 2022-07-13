from django.db import models
from django.urls import reverse


class Task(models.Model):
	list = models.ForeignKey(to='lists.List', on_delete=models.CASCADE, related_name='list', blank=False)
	closed = models.BooleanField(blank=False, default=False)
	title = models.CharField(max_length=20, blank=False)
	details = models.TextField(max_length=125, blank=True)
	due_date = models.DateField(null=True, blank=True)
	favorite = models.BooleanField(null=True, blank=True, default=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("lists:list")

	def close(self):
		self.closed = True
		self.save()

	def unclose(self):
		self.closed = False
		self.save()

