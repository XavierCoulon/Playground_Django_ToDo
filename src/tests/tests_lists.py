from django.urls import reverse
from pytest_django.asserts import assertRedirects


def test_model_list_str(list):
    assert list.__str__() == list.name


def test_model_list_get_absolute_url(client, user_test):
    assert client.login(email=user_test.email, password="password")
    response = client.post(reverse("lists:create"), {"name": "toto"}, follow=True)
    assertRedirects(response, "/lists/")
