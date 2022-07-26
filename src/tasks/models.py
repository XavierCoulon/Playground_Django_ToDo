from django.db import models
from django.urls import reverse
from datetime import date


class Task(models.Model):
	list = models.ForeignKey(to='lists.List', on_delete=models.CASCADE, related_name='tasks', blank=False)
	closed = models.BooleanField(blank=False, default=False)
	title = models.CharField(max_length=40, blank=False)
	details = models.TextField(max_length=125, blank=True)
	due_date = models.DateField(null=True, blank=True)
	favorite = models.BooleanField(null=True, blank=True, default=False)

	def __str__(self):
		return self.title

	def close(self):
		self.closed = True
		self.save()

	def reopen(self):
		self.closed = False
		self.save()

	def due_date_is_past(self):
		if not self.due_date or self.due_date >= date.today():
			return False
		return True
