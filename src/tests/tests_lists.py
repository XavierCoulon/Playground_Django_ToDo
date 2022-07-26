from django.urls import reverse
from django.utils import translation

from lists.rules import is_list_owner
from lists.models import List


def test_model_list_str(list):
    assert list.__str__() == list.name


def test_create_list_form_valid(client, user):
    translation.activate('fr')
    client.login(email=user.email, password="password")
    client.post(reverse("lists:create"), {"name": "test"}, follow=True)
    liste_created = List.objects.get(name="test")
    assert liste_created.user == user


def test_rules_list(list):
    assert is_list_owner(list.user, list)
