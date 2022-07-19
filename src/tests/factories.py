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
    username = fake.email()
    password = factory.PostGenerationMethodCall('set_password', 'password')
    is_active = True
    is_staff = False
    first_name = fake.name()
    last_name = fake.name()


class ListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = List

    name = fake.name()
    user = factory.SubFactory(UserFactory)


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    list = factory.SubFactory(ListFactory)
    closed = False
    # title = fake.name()
    title = "test"
    details = fake.sentence(nb_words=10)
    due_date = fake.date_object()
    favorite = False



