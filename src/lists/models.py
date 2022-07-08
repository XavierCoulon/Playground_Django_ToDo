from django.db import models
from django.conf import settings
from django.urls import reverse


class List(models.Model):
	name = models.CharField(max_length=20, blank=False)
	user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")

	class Meta:
		unique_together = ["name", "user"]

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("lists:list")



