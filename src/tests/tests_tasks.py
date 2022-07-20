from django.urls import reverse
from pytest_django.asserts import assertRedirects


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


# def test_model_task_get_absolute_url(client, list):
#     assert client.login(email=list.user.email, password="password")
#     response = client.post(reverse("tasks:create", args=[list.id]), {"title": "test"}, follow=True)
#     assertRedirects(response, "/lists/")
