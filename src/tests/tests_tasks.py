from django.urls import reverse
from pytest_django.asserts import assertRedirects

from tasks.rules import is_task_owner


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


def test_model_task_get_absolute_url(client, list):
    assert client.login(email=list.user.email, password="password")
    response = client.post(reverse("tasks:create", args=[list.id]), {"title": "test"}, follow=True)
    assertRedirects(response, "/lists/")


def test_view_taskdelete_get(client, task):
    pass


def test_view_taskdelete_get_success_url(client, task):
    assert client.login(email=task.list.user.email, password="password")
    response = client.post(reverse("tasks:delete", args=[task.id]), follow=True)
    assertRedirects(response, "/lists/")


def test_view_task_close(client, task):
    assert client.login(email=task.list.user.email, password="password")
    response = client.post(reverse("tasks:close", args=[task.id]), follow=True)
    assertRedirects(response, "/lists/")


def test_view_task_reopen(client, task):
    assert client.login(email=task.list.user.email, password="password")
    task.close()
    response = client.post(reverse("tasks:reopen", args=[task.id]), follow=True)
    assertRedirects(response, "/lists/")


def test_rules_task(task):
    assert is_task_owner(task.list.user, task)
