from django.urls import reverse
from pytest_django.asserts import assertRedirects

from lists.rules import is_list_owner


def test_model_list_str(list):
    assert list.__str__() == list.name


def test_model_list_get_absolute_url(client, user):
    assert client.login(email=user.email, password="password")
    response = client.post(reverse("lists:create"), {"name": "toto"}, follow=True)
    assertRedirects(response, "/lists/")


def test_rules_list(list):
    assert is_list_owner(list.user, list)


def test_view_listdelete_get_success_url(client, list):
    assert client.login(email=list.user.email, password="password")
    response = client.post(reverse("lists:delete", args=[list.id]), follow=True)
    assertRedirects(response, "/lists/")
