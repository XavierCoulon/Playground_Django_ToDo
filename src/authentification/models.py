from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError("You must enter an email.")

		user = self.model(email=self.normalize_email(email), **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password, **extra_fields):
		user = self.create_user(email=email, password=password, **extra_fields)
		user.is_staff = True
		user.save()
		return user


class CustomUser(AbstractUser):
	username = None
	email = models.EmailField(unique=True, max_length=255, blank=False)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.email
