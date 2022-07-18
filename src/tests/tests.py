import pytest


@pytest.mark.django_db
def test_user(user_factory):
    user = user_factory.create()
    print(user.is_staff)
    assert not user.is_staff


@pytest.mark.django_db
def test_list(list_factory):
    liste = list_factory.create()
    print(liste)
    print(liste.user.email)
    assert True


