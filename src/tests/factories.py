import factory
from faker import Faker

from lists.models import List
from tasks.models import Task
from django.contrib.auth.models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = fake.email()
    username = fake.name()


class ListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = List

    name = fake.name()
    user = factory.SubFactory(UserFactory)
