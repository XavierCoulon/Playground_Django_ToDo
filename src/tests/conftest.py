import pytest

from pytest_factoryboy import register
from tests.factories import UserFactory, ListFactory, TaskFactory

register(UserFactory)
register(ListFactory)
register(TaskFactory)


@pytest.fixture
def user(db, user_factory):
	user = user_factory.create(password="password")
	return user


@pytest.fixture
def list(db, list_factory):
	return list_factory.create()


@pytest.fixture
def task(db, task_factory):
	return task_factory.create()
