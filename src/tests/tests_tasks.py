import requests

from django.urls import reverse
from pytest_django.asserts import assertRedirects
from django.utils import translation
from pprint import pprint

from tasks.rules import is_task_owner
from tasks.models import Task


def test_model_task_str(task):
    assert task.__str__() == task.title


def test_model_task_close(task):
    task.close()
    assert task.closed


def test_model_task_reopen(task):
    task.reopen()
    assert not task.closed


def test_model_task_due_date_is_past(task):
    assert task.due_date_is_past()
    task.due_date = None
    task.save()
    assert not task.due_date_is_past()


def test_create_task_form_valid(client, list):
    client.login(email=list.user.email, password="password")
    client.post(reverse("tasks:create", args=[list.id]), {"title": "test"}, follow=True)
    task_created = Task.objects.get(title="test")
    assert task_created.list == list


def test_view_task_close(client, task):
    translation.activate('fr')
    assert client.login(email=task.list.user.email, password="password")
    response = client.post(reverse("tasks:close", args=[task.id]), follow=True)
    assertRedirects(response, "/fr/lists/")


def test_view_task_reopen(client, task):
    translation.activate('fr')
    assert client.login(email=task.list.user.email, password="password")
    task.close()
    response = client.post(reverse("tasks:reopen", args=[task.id]), follow=True)
    assertRedirects(response, "/fr/lists/")


def test_rules_task(task):
    assert is_task_owner(task.list.user, task)
