import pytest
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from pytest_factoryboy import register
from tests.factories import UserFactory, ListFactory, TaskFactory

register(UserFactory)
register(ListFactory)
register(TaskFactory)


@pytest.fixture()
def user_test(db, user_factory):
	user = user_factory.create(password="password")
	print(user.password)
	return user


@pytest.fixture
def list(db, list_factory):
	list = list_factory.create()
	return list


@pytest.fixture
def task(db, task_factory):
	task = task_factory.create()
	return task

