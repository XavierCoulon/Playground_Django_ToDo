import pytest
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model

from django.urls import reverse

from django.contrib.auth.models import User
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


@pytest.mark.django_db
def test_login(client, user_test):

    username = 'test@test.com'
    password = 'password'

    new_user = User.objects.create_user(
        username=username,
        email=username,
        password=password,
    )
    new_user.save()
    new_user.is_active = True
    new_user.save()

    new_email_address = EmailAddress(
        user_id=new_user.id,
        email=username,
        verified=True,
        primary=True,
    )
    new_email_address.save()

    user_from_fixture = User.objects.all().first()
    user_from_test = User.objects.all().last()

    user_from_fixture_email = EmailAddress.objects.all().first()
    user_from_test_mail = EmailAddress.objects.all().last()

    # print(f"User from fixture: {user_from_fixture_email.__dict__}")
    # print(f"User details: {user_test.__dict__}")
    #print(f"User from test: {user_from_test_mail.__dict__}")
    #print(f"User details: {new_user.__dict__}")


    #logged_in = client.login(email=username, password=password)
    print(user_test.password)
    logged_in2 = client.login(email=user_test.email, password="password")
    #assert logged_in
    assert logged_in2

    #response = client.post(reverse("account_login"), {"login": new_user.username, "password": "password"}, follow=True)
    #assert response.status_code == 200



# def test_model_task_get_absolute_url(client):
#     url = reverse("lists:list")
#     response = client.get(url)
#     assert response.status_code == 200





# @pytest.mark.django_db
# def test_user(user_factory):
#     user = user_factory.create()
#     print(user.is_staff)
#     count = User.objects.all().count()
#     print(count)
#     assert not user.is_staff
#
#
# @pytest.mark.django_db
# def test_list(list_factory):
#     liste = list_factory.create()
#     print(liste)
#     print(liste.user.email)
#     assert True
#
#
# @pytest.mark.django_db
# def test_task(task_factory):
#     task = task_factory.create()
#     print(task.details)
#     assert True
