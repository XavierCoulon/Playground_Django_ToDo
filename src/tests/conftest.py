import pytest

from pytest_factoryboy import register
from tests.factories import UserFactory, ListFactory

register(UserFactory)
register(ListFactory)


